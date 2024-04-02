from dataclasses import dataclass
from os import path, rename
from tempfile import NamedTemporaryFile, gettempdir
from typing import List

from langchain_community.document_loaders import PyPDFLoader
from streamlit.runtime.uploaded_file_manager import UploadedFile


def filepath(file) -> str:
    """
    Creates a temporary file in the system's temporary directory, writes the
    contents of the provided file object to it, and returns the full path to
    the temporary file. Preserves the filename.

    Args:
       file (File-like object): The file object to be written to a temporary file.

    Returns:
       str: The full path to the temporary file.
    """

    tempdir = gettempdir()
    filepath = path.join(tempdir, file.name)

    with NamedTemporaryFile(dir=tempdir, delete=False) as f:
        f.write(file.getbuffer())
        rename(f.name, filepath)

    return filepath


@dataclass
class File:
    def __init__(self, f: UploadedFile):
        self.name = f.name
        self.kind = f.type
        self.path = filepath(f)

    name: str
    kind: str
    path: str


@dataclass
class Files:
    for_db: List[File]
    in_db: List[File]


# [UploadedFile] -> [File]


def is_same(a: UploadedFile, b: File):
    return a.name == b.name


def preprocess_new_files(new_files: List[UploadedFile], files_for_db: List[File]):
    """
    Identifies and removes any duplicate files from the new_files.
    Non-duplicate files are added to the files_for_db list.

    Args:
        new_files (List[UploadedFile]): List of newly uploaded files.
        files_for_db (List[File]): List of files for the database.

    Returns:
        bool: whether files_for_db updated
    """
    updated = False

    for i, new_file in enumerate(new_files):
        if not any(is_same(new_file, file) for file in files_for_db):
            files_for_db.append(File(new_file))
            updated = True

    return updated


# [File] -> [Documents]


def split_pdf(file: File, splitter):
    pages = PyPDFLoader(file.path).load()
    return splitter.split_documents(pages)


def process(file: File, splitter):
    match file.kind:
        case "application/epub+zip":
            pass
        case "application/pdf":
            return split_pdf(file, splitter)

        case "text/markdown":
            pass
        case "text/plain":
            pass
        case "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            pass
        case "application/x-iwork-pages-sffpages":
            pass


def load_to_database(files_for_db: List[File], splitter, db, embedding_fn):
    for f in files_for_db:
        db.from_documents(process(f, splitter), embedding_fn)

from typing import List

from components.file import File
from langchain_community.document_loaders import PyPDFLoader
from streamlit.runtime.uploaded_file_manager import UploadedFile

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

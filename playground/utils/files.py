from dataclasses import dataclass
from os import path, rename
from tempfile import NamedTemporaryFile, gettempdir
from typing import List

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

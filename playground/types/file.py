from os import path, rename
from tempfile import NamedTemporaryFile, gettempdir
from typing import List

from streamlit.runtime.uploaded_file_manager import UploadedFile


def temp_filepath(file) -> str:
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


class File:
    name: str
    kind: str
    path: str

    def __init__(
        self,
        f: UploadedFile | None = None,
        name: str = "",
        kind: str = "",
        path: str = "",
    ):
        if f is not None:
            self.name = f.name
            self.kind = f.type
            self.path = temp_filepath(f)
        else:
            self.name = name
            self.kind = kind
            self.path = path

    def to_json(self):
        return {"name": self.name, "kind": self.kind, "path": self.path}


class Files:
    for_db: List[File]
    in_db: List[File]

    def __init__(
        self,
        in_db: List[File] = [],
        for_db: List[File] | None = None,
    ):
        if for_db is None:
            self.for_db = in_db[:]
            self.in_db = in_db[:]
        else:
            self.for_db = for_db[:]
            self.in_db = in_db[:]

    def to_json(self):
        return [f.to_json() for f in self.in_db]

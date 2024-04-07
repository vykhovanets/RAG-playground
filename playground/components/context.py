import os

from langchain_community.vectorstores.chroma import Chroma

from .project import Project
from .splitter import SplitterType


class Context:
    def __init__(self, prj: Project, chunk_size: int, overlap: int, temp: int):
        self.splitter = SplitterType.RecursiveCharacter.from_type(chunk_size, overlap)
        self.embed = prj.embed.from_type()
        self.llm = prj.llm.from_type(temp)
        self.mem = prj.mem.from_type(f"hist-{prj.id}-ua")
        self.db = Chroma(
            collection_name=f"col-{prj.id}-ua",
            persist_directory=os.getenv("DB", default="./data/db"),
            embedding_function=self.embed
        )

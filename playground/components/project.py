from typing import List

from pydantic.types import Json

from .embed import EmbedType
from .file import File, Files
from .llm import LLMType
from .mem import MemoryType


class Project:
    def __init__(
        self,
        id: str = "id",
        files_in_db: List[File] = [],
        embed: EmbedType = EmbedType.OPENAI,
        llm: LLMType = LLMType.GPT3,
        mem: MemoryType = MemoryType.CONVBUFF,
    ):
        self.id = id
        self.files = Files(in_db=files_in_db[:], for_db=files_in_db[:])
        self.embed = embed
        self.llm = llm
        self.mem = mem


    def to_json(self):
        return {
            "id": self.id,
            "files": self.files.to_json(),
            "embed": self.embed.value,
            "llm": self.llm.value,
            "mem": self.mem.value,
        }

    @staticmethod
    def from_json(json_content: Json):
        return Project(
            id=json_content["id"],
            files_in_db=[File(**file) for file in json_content["files"]],
            embed=EmbedType(json_content["embed"]),
            llm=LLMType(json_content["llm"]),
            mem=MemoryType(json_content["mem"]),
        )

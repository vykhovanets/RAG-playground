from typing import List

from embed import EmbedType
from file import File, Files
from llm import LLMType


class Project:
    def __init__(
        self,
        id: str = "id",
        summary: str = "summary",
        files_in_db: List[File] = [],
        embedding_function: EmbedType = EmbedType.OPENAI,
        llm: LLMType = LLMType.GPT3,
        chat_history=[],
    ):
        self.id = id
        self.summary = summary
        self.files = Files(in_db=files_in_db[:], for_db=files_in_db[:])
        self.embedding_function = embedding_function
        self.llm = llm
        self.chat_history = chat_history

    def to_json(self):
        return {
            "id": self.id,
            "summary": self.summary,
            "files": self.files.to_json(),
            "embedding_function": self.embedding_function.value,
            "llm": self.llm.value,
            "chat_history": self.chat_history,
        }

    @staticmethod
    def from_json(json_content):
        return Project(
            id=json_content["id"],
            summary=json_content["summary"],
            files_in_db=[File(**file) for file in json_content["files"]],
            embedding_function=EmbedType(json_content["embedding_function"]),
            llm=LLMType(json_content["llm"]),
            chat_history=json_content.get("chat_history", []),
        )


# print("asd")
# p = Project(files_in_db=[File(name="hello", kind="por", path="./asdasd")])
# js = p.to_json()
# print(js)
# p1 = Project.from_json(js)
# print(p1.to_json())

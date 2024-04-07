from enum import Enum

from langchain_openai import OpenAIEmbeddings


class EmbedType(str, Enum):
    OPENAI = "openai"

    def from_type(self):
        # match type:
        #     case EmbedType.OPENAI:
        return OpenAIEmbeddings()

from enum import Enum

from langchain.text_splitter import RecursiveCharacterTextSplitter


class SplitterType(str, Enum):
    RecursiveCharacter = "RecursiveCharacterTextSplitter"

    def from_type(self, chunk_size: int, overlap: int):
        # match type:
        #     case SplitterType.RecursiveCharacter:
        return RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=overlap,
            separators=["\n\n", "\n", "(?<=\\. )", " ", ""],
        )

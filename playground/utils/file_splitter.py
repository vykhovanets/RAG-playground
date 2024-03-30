from langchain.text_splitter import RecursiveCharacterTextSplitter


def create_splitter(splitter_type: str, chunk_size: int, overlap: int):
    match splitter_type:
        case _:
            return RecursiveCharacterTextSplitter(
                chunk_size=chunk_size,
                chunk_overlap=overlap,
                separators=["\n\n", "\n", "(?<=\\. )", " ", ""],
            )

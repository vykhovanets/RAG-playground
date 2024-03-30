import chromadb
from langchain_community.vectorstores import Chroma


def get_db_instance(collection_name: str):
    client = chromadb.PersistentClient()
    client.get_or_create_collection(name=collection_name)
    return Chroma(
        client=client,
        collection_name=collection_name,
    )

from enum import Enum
import os

from langchain.memory import ConversationBufferMemory
from langchain_community.chat_message_histories.file import FileChatMessageHistory

class MemoryType(str, Enum):
    CONVBUFF = "ConversationBuffer"

    def from_type(self, id: str) -> ConversationBufferMemory:
        histories_dir = os.getenv("HISTORIES_DIR", default="./data/histories")
        path = os.path.join(histories_dir, f"{id}.json")
        hist = FileChatMessageHistory(path)

        # match type:
        #     case MemoryType.CONVBUFF:

        return ConversationBufferMemory(chat_memory=hist, memory_key="chat_history", return_messages=True)


if __name__ == "__main__":
    mem = MemoryType.CONVBUFF.from_type("asd")

    # print(mem.to_json())

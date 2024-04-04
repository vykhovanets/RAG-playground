from types.file import Files

from components.database import get_instance
from components.file_splitter import create_splitter
from dotenv import load_dotenv
from langchain.memory import ConversationBufferMemory
from langchain_openai import OpenAI, OpenAIEmbeddings
from utils.state import add_to_state, add_to_state_lazy

load_dotenv()

# file loader state
add_to_state("btn_disabled", True)
files = add_to_state("files", Files(in_db=[], for_db=[]))
embedding_fn = add_to_state_lazy("embedding_fn", OpenAIEmbeddings)
db = add_to_state_lazy("db", get_instance, "collection")
splitter = add_to_state_lazy(
    "splitter", create_splitter, "", chunk_size=500, overlap=150
)


# chat state
llm = add_to_state_lazy("llm", OpenAI, temperature=0)
memory = add_to_state_lazy("memory", ConversationBufferMemory)
# conversation = add_to_state_lazy(
#     "conversation",
#     ConversationalRetrievalChain.from_llm,
#     llm=llm,
#     verbose=True,
#     memory=memory,
#     retriever=db.as_retriever(),
# )


# file_loader_widget(files, lc_db, splitter, embedding_fn)
# chat_widget(conversation)

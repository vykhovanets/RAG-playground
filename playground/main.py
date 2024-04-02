from components.api_key_loader import APIKeyLoader
from components.database import get_instance
from components.file_loader import Files
from components.file_splitter import create_splitter
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_openai import OpenAI, OpenAIEmbeddings
from utils.state import add_to_state, add_to_state_lazy
from widgets.chat_widget import chat_widget
from widgets.file_loader_widget import file_loader_widget

APIKeyLoader("config.json").load()

# file loader state
add_to_state("btn_disabled", True)
files = add_to_state("files", Files(in_db=[], for_db=[]))
db = add_to_state_lazy("db", get_instance, "collection")
embedding_fn = add_to_state_lazy("embedding_fn", OpenAIEmbeddings)
splitter = add_to_state_lazy(
    "splitter", create_splitter, "", chunk_size=500, overlap=150
)

# chat state
llm = add_to_state_lazy("llm", OpenAI, temperature=0)
memory = add_to_state_lazy("memory", ConversationBufferMemory)
conversation = add_to_state_lazy(
    "conversation", ConversationChain, llm=llm, verbose=True, memory=memory
)

file_loader_widget(files, db, splitter, embedding_fn)
chat_widget(conversation)

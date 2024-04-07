from components.context import Context
from dotenv import load_dotenv
from langchain.chains.conversation.base import ConversationChain
from utils.persistance import load_project, populate_directories
from utils.state import add_to_state, add_to_state_lazy
from widgets.chat_widget import chat_widget
from widgets.file_widget import file_widget
from langchain.globals import set_verbose

load_dotenv()
populate_directories()

set_verbose(True)
add_to_state("btn_disabled", True)

prj = add_to_state_lazy("project", load_project)

ctx = Context(prj=prj, chunk_size=500, overlap=125, temp=0)
conversation = ConversationChain(llm=ctx.llm, memory=ctx.mem)

file_widget(prj, ctx.db, ctx.splitter, ctx.embed)
chat_widget(conversation)

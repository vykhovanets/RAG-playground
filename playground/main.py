import streamlit as st
from components.context import Context
from dotenv import load_dotenv
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain.globals import set_verbose
from langchain_core.prompts import PromptTemplate
from utils.persistance import load_project, populate_directories
from utils.state import add_to_state, add_to_state_lazy, update_state
from widgets.chat_widget import chat_widget
from widgets.file_widget import file_widget
from widgets.project_widget import project_widget

load_dotenv()
populate_directories()

set_verbose(True)
add_to_state("btn_disabled", True)


prj = add_to_state_lazy("project", load_project)
updated = project_widget()
if updated is not None and updated != prj:
    prj = update_state("project", updated)
    st.rerun()

ctx = Context(prj=prj, chunk_size=500, overlap=125, temp=0)
# conversation = ConversationChain(llm=ctx.llm, memory=ctx.mem)

template = (
    "Combine the chat history and follow up question into "
    "a standalone question. Chat History: {chat_history}"
    "Follow up question: {question}"
)
prompt = PromptTemplate.from_template(template)
# question_generator_chain = LLMChain(llm=ctx.llm, prompt=prompt)

conversation = ConversationalRetrievalChain.from_llm(
    ctx.llm,
    condense_question_prompt=prompt,
    retriever=ctx.db.as_retriever(
        search_type="mmr", search_kwargs={"k": 5, "fetch_k": 50}
    ),
    memory=ctx.mem,
    chain_type="stuff",
)

file_widget(prj, ctx.db, ctx.splitter, ctx.embed)
chat_widget(conversation)

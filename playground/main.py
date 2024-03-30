import streamlit as st
from langchain_openai import OpenAIEmbeddings
from utils.api_key_loader import APIKeyLoader
from utils.db import get_db_instance
from utils.file_splitter import create_splitter
from utils.files import Files
from widgets.file_loader_widget import file_loader_widget

APIKeyLoader("config.json").load()

# st.title("Document Loading App")


def add_to_state(key: str, value):
    if key not in st.session_state:
        st.session_state[key] = value


def add_to_state_lazy(key: str, func, *args, **kwargs):
    if key not in st.session_state:
        st.session_state[key] = func(*args, **kwargs)


add_to_state("files", Files(in_db=[], for_db=[]))
add_to_state("btn_disabled", True)
add_to_state_lazy("db", get_db_instance, "collection")
add_to_state_lazy("splitter", create_splitter, "", chunk_size=500, overlap=150)
add_to_state_lazy("embedding_fn", OpenAIEmbeddings)

files = st.session_state.files
db = st.session_state.db
splitter = st.session_state.splitter
embedding_fn = st.session_state.embedding_fn

file_loader_widget(files, db, splitter, embedding_fn)

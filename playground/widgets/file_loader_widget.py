import pandas as pd
import streamlit as st
from utils.file_loader import load_to_database, preprocess_new_files


def btn_disable():
    st.session_state.btn_disabled = True


def btn_enable(updated: bool):
    if st.session_state.btn_disabled and updated:
        st.session_state.btn_disabled = False


def file_loader_widget(files, db, splitter, embedding_fn):
    file_loader_expander = st.expander("File loader")
    with file_loader_expander:
        new_files = st.file_uploader("Upload documents", accept_multiple_files=True)
        if new_files is not None:
            result = preprocess_new_files(new_files, files.for_db)
            btn_enable(result)

        clicked = st.button(
            "Add to VectorDB",
            on_click=btn_disable,
            disabled=st.session_state.btn_disabled,
            use_container_width=True,
        )

        if clicked:
            diff = [file for file in files.for_db if file not in files.in_db]

            load_to_database(diff, splitter, db, embedding_fn)

            files.in_db.extend(diff)

        df = pd.DataFrame(
            data=[file.name for file in files.in_db], columns=["VectorDB content"]
        )
        st.data_editor(df, disabled=True, use_container_width=True, hide_index=True)

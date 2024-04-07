import streamlit as st
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage
from streamlit.delta_generator import DeltaGenerator


def display_message(container: DeltaGenerator, message: BaseMessage):
    match message:
        case HumanMessage():
            with container.chat_message("user", avatar="./assets/user.png"):
                st.markdown(message.content)
        case AIMessage():
            with container.chat_message("ai", avatar="./assets/ai.png"):
                st.markdown(message.content)
        case _:
            with container.chat_message("unknown"):
                st.markdown(message.content)


def show_history(container: DeltaGenerator, messages):
    for message in messages:
        display_message(container, message)


def chat_widget(conversation):
    with st.container():
        history_container = st.container(height=500, border=True)
        show_history(history_container, conversation.memory.buffer_as_messages)

        if prompt := st.chat_input("Say something"):
            display_message(history_container, HumanMessage(content=prompt))
            conversation.predict(input=prompt)
            display_message(
                history_container, conversation.memory.buffer_as_messages[-1]
            )

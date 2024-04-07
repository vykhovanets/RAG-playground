[back](../README.md)

{{TOC}}

# Streamlit

# Iteration #1

_The goal of the first iteration is to have local application which will make API calls to LLM providers_

Main things which will be covered here: Streamlit app architecture, standard development workflow, state management, persistence, best practices.

- `streamlit` is a server application
- On every save of the `.py` file and on every user ineraction with the app, the whole script reruns. Callbacks (`on_change`, ` on_click`) are computed before the rest of the script.
- `st.sidebar.selectbox` puts select box in left sidebar.
- To run method only once, there is `@st.cache_data` decorator.
- On page refresh session state get cleaned

No success:
- `st.cache_data` creates a new copy of the data at each function call
- `st.cache_resource` returns the cached object itself

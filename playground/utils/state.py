from streamlit import session_state


def add_to_state(key: str, value):
    if key not in session_state:
        session_state[key] = value

    return session_state[key]

def update_state(key: str, value):
    session_state[key] = value
    return session_state[key]

def add_to_state_lazy(key: str, func, *args, **kwargs):
    if key not in session_state:
        session_state[key] = func(*args, **kwargs)

    return session_state[key]

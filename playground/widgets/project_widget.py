import streamlit as st
from components.project import Project
from utils.persistance import get_active, new_project, project_list, load_project


def project_widget() -> Project | None:
    new_label = "Add New"
    projects = project_list()
    projects.insert(0, new_label)

    active = get_active()
    index = 0 if active is None else projects.index(active)

    option = st.selectbox(
        "Select project",
        projects,
        index=index,
        label_visibility="collapsed",
    )
    if option is not None:
        if option == new_label:
            return new_project()
        elif projects.index(option) != index:
            return load_project(option)

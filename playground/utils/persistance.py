import json
import os
from datetime import datetime
from pathlib import Path
from typing import List

from components.project import Project


def populate_directories():
    projects_dir()
    histories_dir()
    db_dir()


def projects_dir():
    path = Path(os.getenv("PROJECTS_DIR", default="./data/projects"))
    path.mkdir(parents=True, exist_ok=True)
    return path


def histories_dir():
    path = Path(os.getenv("HISTORIES_DIR", default="./data/histories"))
    path.mkdir(parents=True, exist_ok=True)
    return path


def db_dir():
    path = Path(os.getenv("DB", default="./data/db"))
    path.mkdir(parents=True, exist_ok=True)
    return path


def set_active(filename: str):
    (projects_dir() / "latest.txt").write_text(filename)


def get_active() -> str | None:
    path = projects_dir() / "latest.txt"
    return None if not path.exists() else path.read_text()


def project_list() -> List[str]:
    return [f for f in os.listdir(projects_dir()) if f.endswith(".json")]


def generate_id():
    return f"{datetime.now().strftime("%Y%m%d%H%M%S")}"


def save_project(prj: Project):
    filename = f"{prj.id}.json"
    Path(projects_dir() / filename).write_text(json.dumps(prj.to_json()))
    return filename


def new_project() -> Project:
    p = Project(id=generate_id())
    set_active(save_project(p))
    return p


def load_project(filename: str | None = None) -> Project:
    """
    try to load if correct filename is provided.
    if not, loads an active project if it is present
    creates new otherwise
    """

    if (
        filename is not None
        and (path := projects_dir() / filename).exists()
        and len(data := json.loads(path.read_text())) > 0
    ):
        p = Project.from_json(json.loads(path.read_text()))
        set_active(filename)
    elif (
        (filename := get_active()) is not None
        and (path := projects_dir() / filename).exists()
        and len(data := json.loads(path.read_text())) > 0
    ):
        p = Project.from_json(data)
    else:
        p = new_project()
    return p

import json
import os
from datetime import datetime
from pathlib import Path
from types.project import Project
from typing import List

from dotenv import load_dotenv


def generate_id():
    return datetime.now().strftime("%Y.%m.%d %H:%M:%S")


class PersistanceManager:
    def __init__(self):
        self.active_project = ""

        load_dotenv()
        self.projects_dir = os.getenv("PROJECTS_DIR", default="./data/projects")
        os.makedirs(self.projects_dir, exist_ok=True)

        self.projects = os.listdir(self.projects_dir)

    def project_list(self) -> List[str]:
        return self.projects

    def add_new_project(self, **kwargs) -> Project:
        self.active_project = os.path.join(self.projects_dir, f"{generate_id()}.json")
        self.projects.append(self.active_project)
        Path(self.active_project).touch()
        return Project(**kwargs)

    def get_project(self, filename: str) -> Project:
        self.active_project = filename
        with open(filename, "r") as f:
            data = json.load(f)
            return Project.from_json(data)

    def save_project(self, project: Project):
        path = os.path.join(self.projects_dir, self.active_project)
        with open(path, "w") as f:
            json.dump(project.to_json(), f)

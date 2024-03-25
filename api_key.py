import json
import os


class APIKeyLoaderException(Exception):
    def __init__(self, config):
        self.config = config

    def __str__(self):
        return f"{__class__.__name__}: can't load keys from '{self.config}'"


class APIKeyLoader:
    """
    Loads API keys from config.json into evironment
    """

    def __init__(self, json_config_path: str):
        self.config = json_config_path

    def load(self):
        try:
            with open(self.config, "r") as f:
                config = json.load(f)
                for key, value in config.items():
                    print(f"{__class__.__name__}: load '{key}'")
                    os.environ[key] = value
        except (FileNotFoundError, IOError, json.JSONDecodeError):
            raise APIKeyLoaderException(self.config)

import os.path
from typing import Optional

import yaml


def load_pipeline(config_path: str) -> Optional[dict]:
    if not os.path.exists(config_path):
        raise FileNotFoundError

    with open(config_path, "rb") as conf_file:
        data = yaml.safe_load(conf_file)

    try:
        steps = data["steps"]
        if not isinstance(steps, list):
            raise TypeError("steps must be a list of dictionaries")

        return data
    except KeyError:
        raise ValueError("steps list is required")

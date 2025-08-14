import os.path
from typing import Optional

from yaml import safe_load


def load_pipeline(config_path: str) -> Optional[dict]:
    """
    Used to load the config file as a dictionary
    :param config_path: path to pipeline.yaml
    :return: a dictionary with the pipeline configuration
    """
    if not os.path.exists(config_path):
        raise FileNotFoundError

    with open(config_path, "rb") as conf_file:
        data = safe_load(conf_file)

    try:
        steps = data["steps"]
        if not isinstance(steps, list):
            raise TypeError("steps must be a list of dictionaries")

        return data
    except KeyError:
        raise ValueError("steps list is required")

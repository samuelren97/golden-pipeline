import argparse
import os.path
from typing import Optional

from yaml import safe_load


def load_pipeline(
    args: argparse.Namespace,
) -> Optional[dict]:
    """
    Used to load the config file as a dictionary
    :param args: parsed argparse arguments
    :return: a dictionary with the pipeline configuration
    """
    config_path = "pipeline.yaml"
    if args.config:
        config_path = args.config

    if not os.path.exists(config_path):
        raise FileNotFoundError

    with open(config_path, "rb") as conf_file:
        data = safe_load(conf_file)
        if args.verbose:
            print(f"Pipeline config content:\n{data}")

    try:
        steps = data["steps"]

        if not isinstance(steps, list):
            raise TypeError("steps must be a list of dictionaries")

        return data
    except KeyError:
        raise ValueError("steps list is required")

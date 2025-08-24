import argparse
import os.path
from typing import Optional

from yaml import safe_load

from goldenpipeline.logger import debug


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

    with open(config_path, "r") as conf_file:
        pipeline_content = conf_file.read()
        data = safe_load(pipeline_content)

        try:
            v: dict = data["vars"]
            for key in v.keys():
                pipeline_content = pipeline_content.replace(
                    "${" + key + "}",
                    v[key],
                )

            data = safe_load(pipeline_content)
        finally:
            pass

        if args.verbose:
            debug(f"Pipeline config content:\n{data}")

    try:
        steps = data["steps"]

        if not isinstance(steps, list):
            raise TypeError("steps must be a list of dictionaries")

        return data
    except KeyError:
        raise ValueError("steps list is required")

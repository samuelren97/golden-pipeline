import os.path
import shutil

from goldenpipeline.registry import register_step
from goldenpipeline.steps.utils import validate_step_required_params


def run_copy(params: dict) -> None:
    src = f"tmp/{params["src"]}"
    dest = f"tmp/{params["dest"]}"
    shutil.copy(src, dest)


@register_step("copy")
def copy_step(params: dict) -> None:
    required_params = [
        "src",
        "dest",
    ]

    params_list = list(params.keys())

    print("Validating pipeline copy parameters...")
    validate_step_required_params(params_list, required_params)

    print("Validating that the source file exists...")
    if not os.path.exists(f"tmp/{params["src"]}"):
        raise FileNotFoundError(f"File {params["src"]} does not exist")

    print("Running copy")
    run_copy(params)

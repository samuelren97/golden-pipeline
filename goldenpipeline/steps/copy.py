import os.path
import shutil

from goldenpipeline.registry import register_step
from goldenpipeline.steps.utils import validate_step_required_params


def run_copy(params: dict, tmp_dir: str) -> None:
    src = f"{tmp_dir}/{params["src"]}"
    dest = f"{tmp_dir}/{params["dest"]}"
    shutil.copy(src, dest)


@register_step("copy")
def copy_step(
    params: dict,
    is_verbose: bool,
    is_dry_run: bool,
    tmp_dir: str,
) -> None:
    required_params = [
        "src",
        "dest",
    ]

    params_list = list(params.keys())

    if is_verbose:
        print("Validating pipeline copy parameters...")
    validate_step_required_params(params_list, required_params)

    if not is_dry_run:
        if is_verbose:
            print("Validating that the source file exists...")
        if not os.path.exists(f"{tmp_dir}/{params["src"]}"):
            raise FileNotFoundError(f"File {params["src"]} does not exist")

    print("Running copy...")

    if not is_dry_run:
        run_copy(params, tmp_dir)
    print("Copy was successful")

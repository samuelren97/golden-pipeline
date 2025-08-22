import os.path
import shutil

from goldenpipeline.logger import debug, info
from goldenpipeline.registry import register_step
from goldenpipeline.steps.utils import validate_step_required_params


def run_copy(params: dict) -> None:
    src = params["src"]
    dest = params["dest"]
    shutil.copy(src, dest)


@register_step("copy")
def copy_step(
        params: dict,
        is_verbose: bool,
        is_dry_run: bool,
) -> None:
    """
    Step that copies a file
    :param params: Parameter dictionary
    :param is_verbose: Enables verbose logs
    :param is_dry_run: Enables dry run
    :return:
    """
    required_params = [
        "src",
        "dest",
    ]

    params_list = list(params.keys())

    if is_verbose:
        debug("Validating pipeline copy parameters...")
    validate_step_required_params(params_list, required_params)

    if not is_dry_run:
        if is_verbose:
            debug("Validating that the source file exists...")
        if not os.path.exists(params["src"]):
            raise FileNotFoundError(f"File {params["src"]} does not exist")

    info("Running copy...")

    if not is_dry_run:
        run_copy(params)
    info("Copy was successful")

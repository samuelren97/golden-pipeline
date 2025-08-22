import subprocess

from goldenpipeline.InvalidConfigError import InvalidConfigError
from goldenpipeline.logger import debug, info
from goldenpipeline.registry import register_step
from goldenpipeline.steps.utils import validate_step_required_params


def validate_parameter_values(params: dict) -> None:
    for key in list(params.keys()):
        if not isinstance(params[key], str):
            raise InvalidConfigError(
                "checkout parameter values must be strings, type is: "
                f"{type(params[key])}"
            )


def run_checkout(params: dict) -> None:
    repo = params["repo"]
    ref = params["ref"]

    subprocess.run(["git", "clone", "--branch", ref, repo], check=True)


@register_step("checkout")
def checkout_step(
        params: dict,
        is_verbose: bool,
        is_dry_run: bool,
) -> None:
    """
    Step that checkout a local or remote git repository
    :param params: Parameter dictionary
    :param is_verbose: Enables verbose logs
    :param is_dry_run: Enables dry run
    :return:
    """
    required_params = [
        "repo",
        "ref",
    ]

    params_list = list(params.keys())

    if is_verbose:
        debug("Validating pipeline checkout parameters...")
    validate_step_required_params(params_list, required_params)

    if is_verbose:
        debug("Validating parameter values...")
    validate_parameter_values(params)

    info("Running checkout...")

    if not is_dry_run:
        run_checkout(params)
    info("Checkout done successfully")

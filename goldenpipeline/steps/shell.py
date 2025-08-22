import os
import subprocess

from goldenpipeline.InvalidConfigError import InvalidConfigError
from goldenpipeline.logger import debug, info
from goldenpipeline.registry import register_step
from goldenpipeline.steps.utils import validate_step_required_params


@register_step("shell")
def shell_step(
    params: dict,
    is_verbose: bool,
    is_dry_run: bool,
) -> None:
    """
    Shell step runs a command in the default OS shell.
    :param params: Parameter dictionary
    :param is_verbose: Enables verbose logs
    :param is_dry_run: Enables dry run
    :return:
    """
    required_params = [
        "command",
        "stop_on_error",
        "cwd",
    ]

    params_list = list(params.keys())
    n_params = params
    if "stop_on_error" not in params_list:
        n_params["stop_on_error"] = True

    if "cwd" not in params_list:
        n_params["cwd"] = os.getcwd()

    n_params_list = list(n_params.keys())

    if is_verbose:
        debug("Validating pipeline shell parameters...")
    validate_step_required_params(n_params_list, required_params)

    if is_verbose:
        debug("Validating command...")
    if not isinstance(n_params["command"], str):
        raise InvalidConfigError("Command must be of type string")
    command = n_params["command"].split(" ")

    if is_verbose:
        debug("Validating stop_on_error parameter")
    if not isinstance(n_params["stop_on_error"], bool):
        raise InvalidConfigError("stop_on_error must be of type bool")

    info("Running command...")
    if not is_dry_run:
        subprocess.run(
            command,
            check=n_params["stop_on_error"],
            shell=True,
            cwd=n_params["cwd"],
        )
    info("Command ran successfully")

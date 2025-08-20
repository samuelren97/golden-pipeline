import subprocess
from idlelib.config import InvalidConfigType

from goldenpipeline.registry import register_step
from goldenpipeline.steps.utils import validate_step_required_params


@register_step("shell")
def shell_step(
    params: dict,
    is_verbose: bool,
    is_dry_run: bool,
    tmp_dir: str,
) -> None:
    required_params = [
        "command",
        "stop_on_error",
    ]

    params_list = list(params.keys())
    n_params = params
    if "stop_on_error" not in params_list:
        n_params["stop_on_error"] = True

    n_params_list = list(n_params.keys())

    if is_verbose:
        print("Validating pipeline shell parameters...")
    validate_step_required_params(n_params_list, required_params)

    if is_verbose:
        print("Validating command...")
    if not isinstance(n_params["command"], str):
        raise InvalidConfigType("Command must be of type string")
    command = n_params["command"].split(" ")

    if is_verbose:
        print("Validating stop_on_error parameter")
    if not isinstance(n_params["stop_on_error"], bool):
        raise InvalidConfigType("stop_on_error must be of type bool")

    print("Running command...")
    if not is_dry_run:
        subprocess.run(
            command,
            check=n_params["stop_on_error"],
            shell=True,
            cwd=tmp_dir,
        )
    print("Command ran successfully")

import os
import subprocess

from goldenpipeline.logger import debug, info
from goldenpipeline.registry import register_step
from goldenpipeline.steps.utils import validate_step_required_params


@register_step("docker-compose")
def docker_compose_step(
        params: dict,
        is_verbose: bool,
        is_dry_run: bool,
) -> None:
    required_params = [
        "file",
        "build",
    ]

    params_list = list(params.keys())
    n_params = params

    if "build" not in params_list:
        n_params["build"] = False

    if is_verbose:
        debug("Validating pipeline copy parameters...")
    validate_step_required_params(params_list, required_params)

    info("Running docker compose...")
    command = [
        "docker",
        "compose",
        "-f",
        n_params["file"],
        "up",
        "-d"
    ]

    if n_params["build"]:
        command.append("--build")

    if is_verbose:
        debug(f"Running command {command}")

    if not is_dry_run:
        subprocess.run(
            command,
            shell=os.name == "nt",
            cwd=".",
        )

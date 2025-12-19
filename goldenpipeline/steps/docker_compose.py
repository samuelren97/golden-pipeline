import os
import subprocess

from goldenpipeline.logger import debug, info
from goldenpipeline.registry import register_step
from goldenpipeline.steps.utils import (print_sub_title,
                                        validate_step_required_params)


@register_step("docker-compose")
def docker_compose_step(
    params: dict,
    is_verbose: bool,
    is_dry_run: bool,
) -> None:
    required_params = [
        "up" "file",
        "build",
        "cwd",
    ]

    params_list = list(params.keys())
    n_params = params

    if "up" not in params_list:
        n_params["up"] = True

    if "build" not in params_list:
        n_params["build"] = False

    if "cwd" not in params_list:
        n_params["cwd"] = "."

    params_list = list(n_params.keys())

    if is_verbose:
        debug("Validating pipeline copy parameters...")
    validate_step_required_params(params_list, required_params)

    file = n_params["file"]
    print_sub_title(f"Compose => {file}")

    info("Running docker compose...")

    if n_params["up"]:
        command = ["docker", "compose", "-f", file, "up", "-d"]
    else:
        command = ["docker", "compose", "-f", file, "down", "--rmi", "local"]

    if n_params["build"]:
        command.append("--build")

    if is_verbose:
        debug(f"Running command {command}")

    if not is_dry_run:
        subprocess.run(
            command,
            shell=os.name == "nt",
            cwd=n_params["cwd"],
        )

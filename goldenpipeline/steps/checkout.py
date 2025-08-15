import os
import subprocess
from idlelib.config import InvalidConfigType

from goldenpipeline.registry import register_step
from goldenpipeline.steps.utils import validate_step_required_params


def validate_parameter_values(params: dict) -> None:
    for key in list(params.keys()):
        if type(params[key]) != str:
            raise InvalidConfigType("checkout parameter values must be strings, type is: "
                                    f"{type(params[key])}")


def run_checkout(params: dict) -> None:
    repo_path = params["repo_path"]
    ref = params["ref"]

    if not os.path.exists(repo_path):
        raise FileNotFoundError(f"Repo path does not exist: {repo_path}")

    subprocess.run(["git", "-C", repo_path, "fetch", "origin"], check=False)
    subprocess.run(["git", "-C", repo_path, "checkout", ref], check=True)
    subprocess.run(["git", "-C", repo_path, "pull"], check=False)


@register_step("checkout")
def checkout_step(params: dict):
    required_params = [
        "repo_path",
        "ref",
    ]

    params_list = list(params.keys())

    print("Validating pipeline checkout steps...")
    validate_step_required_params(params_list, required_params)

    print("Validating parameter values...")
    validate_parameter_values(params)

    print("Running checkout...")
    run_checkout(params)
    print("Checkout done successfully")

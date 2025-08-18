import subprocess
from idlelib.config import InvalidConfigType

from goldenpipeline.registry import register_step
from goldenpipeline.steps.utils import validate_step_required_params


def validate_parameter_values(params: dict) -> None:
    for key in list(params.keys()):
        if not isinstance(params[key], str):
            raise InvalidConfigType("checkout parameter values must be strings, type is: "
                                    f"{type(params[key])}")


def run_checkout(params: dict) -> None:
    repo = params["repo"]
    ref = params["ref"]

    subprocess.run(["git", "-C", "tmp", "clone", repo, "."], check=True)
    subprocess.run(["git", "-C", "tmp", "checkout", ref], check=True)


@register_step("checkout")
def checkout_step(params: dict) -> None:
    required_params = [
        "repo",
        "ref",
    ]

    params_list = list(params.keys())

    print("Validating pipeline checkout parameters...")
    validate_step_required_params(params_list, required_params)

    print("Validating parameter values...")
    validate_parameter_values(params)

    print("Running checkout...")
    run_checkout(params)
    print("Checkout done successfully")

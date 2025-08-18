import os.path

from goldenpipeline.registry import register_step
from goldenpipeline.steps.utils import validate_step_required_params


def run_transform(params: dict) -> None:
    file = f"tmp/{params["file"]}"
    value_list: list[dict] = params["values"]

    content = ""
    with open(file, "r") as f:
        content = f.read()

    for val in value_list:
        key = list(val.keys())[-1]
        to_replace = "${" + key + "}"
        new_val = val[key]

        content = content.replace(to_replace, new_val)

    with open(file, "w") as f:
        f.write(content)


@register_step("transform")
def transform_step(params: dict) -> None:
    required_params = [
        "file",
        "values",
    ]

    params_list = list(params.keys())

    print("Validating pipeline transform parameters...")
    validate_step_required_params(params_list, required_params)

    if not os.path.exists(f"tmp/{params["file"]}"):
        raise FileNotFoundError(f"File {params["file"]} does not exist")

    run_transform(params)

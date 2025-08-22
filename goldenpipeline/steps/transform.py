import os.path

from goldenpipeline.logger import debug, info
from goldenpipeline.registry import register_step
from goldenpipeline.steps.utils import validate_step_required_params


def run_transform(params: dict, tmp_dir: str) -> None:
    file = f"{tmp_dir}/{params["file"]}"
    value_list: list[dict] = params["values"]

    content = ""
    with open(file, "r") as f:
        content = f.read()

    for val in value_list:
        key = list(val.keys())[-1]
        new_val = val[key]

        content = content.replace(key, new_val)

    with open(file, "w") as f:
        f.write(content)


@register_step("transform")
def transform_step(
    params: dict,
    is_verbose: bool,
    is_dry_run: bool,
    tmp_dir: str,
) -> None:
    """
    Transforms text in a file with a given search pattern.
    :param params: Parameter dictionary
    :param is_verbose: Enables verbose logs
    :param is_dry_run: Enables dry run
    :param tmp_dir: Specifies the tmp working directory
    :return:
    """
    required_params = [
        "file",
        "values",
    ]

    params_list = list(params.keys())

    if is_verbose:
        debug("Validating pipeline transform parameters...")
    validate_step_required_params(params_list, required_params)

    if not is_dry_run:
        if is_verbose:
            debug("Validating that the file exists...")
        if not os.path.exists(f"{tmp_dir}/{params["file"]}"):
            raise FileNotFoundError(f"File {params["file"]} does not exist")

    info("Running transform...")
    if not is_dry_run:
        run_transform(params, tmp_dir)
    info("Transform done successfully")

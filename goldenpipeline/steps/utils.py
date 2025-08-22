from goldenpipeline.InvalidConfigError import InvalidConfigError


def validate_step_required_params(
    params: list[str], required_params: list[str]
) -> None:
    if set(params) != set(required_params):
        message = (
            f"Not all required parameters were set:\n"
            f"Specified: {params}\n"
            f"Required: {required_params}"
        )
        raise InvalidConfigError(message)

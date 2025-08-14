from idlelib.config import InvalidConfigType
from typing import Any

from goldenpipeline.registry import STEP_REGISTRY


def validate_pipeline_steps(steps: list[dict[str, Any]]) -> None:
    for step in steps:
        keys = list(step.keys())
        if len(keys) != 1:
            raise InvalidConfigType("a step must contain a single key")

        key = keys[0]
        try:
            _ = STEP_REGISTRY[key]
        except KeyError:
            raise InvalidConfigType(f"invalid step: {key}")


def execute_pipeline(steps: list[dict[str, Any]]) -> None:
    validate_pipeline_steps(steps)
    for step in steps:
        key = list(step.keys())[0]
        params = step[key]
        STEP_REGISTRY[key](params)

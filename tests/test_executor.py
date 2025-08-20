from idlelib.config import InvalidConfigType

import pytest

from goldenpipeline.executor import execute_pipeline
from goldenpipeline.loader import load_pipeline
from goldenpipeline.registry import STEP_REGISTRY, register_step
from tests.pipeline_content_test_cases import (
    pipeline_content_unknown_step,
    pipeline_content_valid_config,
)


def test_valid_steps(tmp_path):
    @register_step("chicken")
    def chicken_step(params):
        pass

    pipeline_path = tmp_path / "pipeline.yaml"
    pipeline_path.write_text(pipeline_content_valid_config)
    pipeline = load_pipeline(str(pipeline_path))

    try:
        execute_pipeline(pipeline["steps"])
    finally:
        STEP_REGISTRY.clear()


def test_unknown_step_invalid_config_type(tmp_path):
    pipeline_path = tmp_path / "pipeline.yaml"
    pipeline_path.write_text(pipeline_content_unknown_step)
    pipeline = load_pipeline(str(pipeline_path))

    with pytest.raises(InvalidConfigType):
        execute_pipeline(pipeline["steps"])

import importlib
import pkgutil

import pytest

from goldenpipeline import steps
from goldenpipeline.InvalidConfigError import InvalidConfigError
from goldenpipeline.executor import execute_pipeline
from goldenpipeline.loader import load_pipeline
from goldenpipeline.registry import STEP_REGISTRY
from tests.args import init_args
from tests.pipeline_content_test_cases import (
    pipeline_content_unknown_step,
    pipeline_content_valid_config,
)

for _, module_name, _ in pkgutil.iter_modules(steps.__path__):
    importlib.import_module(f"goldenpipeline.steps.{module_name}")


def test_valid_steps(tmp_path):
    args = init_args()

    pipeline_path = tmp_path / "pipeline.yaml"
    pipeline_path.write_text(pipeline_content_valid_config)
    args.config = str(pipeline_path)
    pipeline = load_pipeline(args)

    print(f"Steps: {STEP_REGISTRY}")

    try:
        execute_pipeline(pipeline["steps"], args)
    finally:
        STEP_REGISTRY.clear()


def test_unknown_step_invalid_config_type(tmp_path):
    args = init_args()
    pipeline_path = tmp_path / "pipeline.yaml"
    args.config = str(pipeline_path)
    pipeline_path.write_text(pipeline_content_unknown_step)
    pipeline = load_pipeline(args)

    with pytest.raises(InvalidConfigError):
        execute_pipeline(pipeline["steps"], args)

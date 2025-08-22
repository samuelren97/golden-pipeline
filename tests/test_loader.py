import pytest

from goldenpipeline import loader
from tests.args import init_args
from tests.pipeline_content_test_cases import (pipeline_content_steps_missing,
                                               pipeline_content_steps_not_list,
                                               pipeline_content_valid_config)


def test_valid_config(tmp_path):
    args = init_args()
    pipeline_path = tmp_path / "pipeline.yaml"
    args.config = str(pipeline_path)
    pipeline_path.write_text(pipeline_content_valid_config)

    expected = {"steps": [{"checkout": {"ref": "main", "repo": "./src"}}]}

    config = loader.load_pipeline(args)
    assert config == expected


def test_file_not_found_error():
    args = init_args()
    with pytest.raises(FileNotFoundError):
        args.config = "chicken"
        loader.load_pipeline(args)


def test_steps_missing_value_error(tmp_path):
    args = init_args()
    pipeline_path = tmp_path / "pipeline.yaml"
    args.config = str(pipeline_path)
    pipeline_path.write_text(pipeline_content_steps_missing)

    with pytest.raises(ValueError):
        loader.load_pipeline(args)


def test_steps_not_list_type_error(tmp_path):
    args = init_args()
    pipeline_path = tmp_path / "pipeline.yaml"
    args.config = str(pipeline_path)
    pipeline_path.write_text(pipeline_content_steps_not_list)

    with pytest.raises(TypeError):
        loader.load_pipeline(args)

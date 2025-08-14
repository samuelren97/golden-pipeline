import pytest

from .. import loader

test_case_valid_config = """
steps:
    - checkout:
        repo: ./src
"""

test_case_steps_missing = """
test:
    one: hey
"""

test_case_steps_not_list = """
steps:
    one: hey
"""


def test_valid_config(tmp_path):
    file_path = tmp_path / "pipeline.yaml"
    file_path.write_text(test_case_valid_config)

    expected = {
        "steps": [
            {
                "checkout": {
                    "repo": "./src"
                }
            }
        ]
    }

    config = loader.load_pipeline(str(file_path))
    assert config == expected


def test_file_not_found_error():
    with pytest.raises(FileNotFoundError):
        loader.load_pipeline("")


def test_steps_missing_value_error(tmp_path):
    file_path = tmp_path / "pipeline.yaml"
    file_path.write_text(test_case_steps_missing)

    with pytest.raises(ValueError):
        loader.load_pipeline(str(file_path))


def test_steps_not_list_type_error(tmp_path):
    file_path = tmp_path / "pipeline.yaml"
    file_path.write_text(test_case_steps_not_list)

    with pytest.raises(TypeError):
        loader.load_pipeline(str(file_path))

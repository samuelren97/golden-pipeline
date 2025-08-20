import pytest

from goldenpipeline.registry import STEP_REGISTRY, register_step


def test_add_step_to_registry_one_registry():
    @register_step("chicken")
    def chicken_step():
        pass

    try:
        assert len(STEP_REGISTRY) == 1
    finally:
        STEP_REGISTRY.clear()


def test_check_name_in_registry():
    @register_step("chicken")
    def chicken_step():
        pass

    try:
        _ = STEP_REGISTRY["chicken"]
    finally:
        STEP_REGISTRY.clear()


def test_duplicate_step_name_key_error():
    with pytest.raises(ValueError):

        @register_step("chicken")
        def chicken_step_1():
            pass

        @register_step("chicken")
        def chicken_step_2():
            pass

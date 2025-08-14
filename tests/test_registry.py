import pytest

from goldenpipeline.registry import register_step, STEP_REGISTRY


def test_add_step_to_registry_one_registry():
    @register_step("checkout_1")
    def checkout_step():
        pass

    assert len(STEP_REGISTRY) == 1


def test_check_name_in_registry():
    @register_step("checkout_2")
    def checkout_step():
        pass

    _ = STEP_REGISTRY["checkout_2"]


def test_duplicate_step_name_key_error():
    with pytest.raises(ValueError):
        @register_step("checkout_1")
        def checkout_step():
            pass

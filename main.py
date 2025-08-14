from goldenpipeline import loader
from goldenpipeline.executor import execute_pipeline
from goldenpipeline.registry import register_step


@register_step("checkout")
def checkout_step(params: list):
    print(f"checkout keys: {params}")


if __name__ == "__main__":
    pipeline = loader.load_pipeline("pipeline.yaml")
    execute_pipeline(pipeline["steps"])

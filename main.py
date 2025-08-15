import importlib
import pkgutil

from goldenpipeline import steps  # noqa: F401
from goldenpipeline import loader
from goldenpipeline.executor import execute_pipeline

for _, module_name, _ in pkgutil.iter_modules(steps.__path__):
    importlib.import_module(f"goldenpipeline.steps.{module_name}")

if __name__ == "__main__":
    pipeline = loader.load_pipeline("pipeline.yaml")
    execute_pipeline(pipeline["steps"])

import importlib
import os
import pkgutil
import shutil
import stat

from goldenpipeline import loader
from goldenpipeline import steps  # noqa: F401
from goldenpipeline.executor import execute_pipeline

for _, module_name, _ in pkgutil.iter_modules(steps.__path__):
    importlib.import_module(f"goldenpipeline.steps.{module_name}")

if __name__ == "__main__":
    if not os.path.exists("tmp"):
        os.mkdir("tmp", 0o777)
    try:
        pipeline = loader.load_pipeline("pipeline.yaml")
        execute_pipeline(pipeline["steps"])
    finally:
        def on_rm_error(func, path, exc_info):
            os.chmod(path, stat.S_IWRITE)
            func(path)


        shutil.rmtree("tmp", onexc=on_rm_error)

import argparse
import importlib
import pkgutil

from goldenpipeline import loader, steps
from goldenpipeline.executor import execute_pipeline

for _, module_name, _ in pkgutil.iter_modules(steps.__path__):
    importlib.import_module(f"goldenpipeline.steps.{module_name}")


def init_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="A simple CI/CD local and configurable pipeline",
    )

    parser.add_argument(
        "--config",
        help="--config <path> - The configuration file to build the pipeline",
        default="pipeline.yaml",
    )
    parser.add_argument(
        "--verbose",
        help="Enable detail logging",
        action="store_true",
    )
    parser.add_argument(
        "--dry-run",
        help="Simulate the pipeline without actually running the steps",
        action="store_true",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = init_args()
    pipeline = loader.load_pipeline(args)
    execute_pipeline(pipeline["steps"], args=args)

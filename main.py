import argparse
import importlib
import os
import pkgutil
import shutil
import stat

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
    parser.add_argument(
        "--tmp-dir",
        help="Specify the temporary directory to run the pipeline",
        default="tmp",
    )
    return parser.parse_args()


def on_rm_error(func, path, _):
    os.chmod(path, stat.S_IWRITE)
    func(path)


if __name__ == "__main__":
    args = init_args()

    if not os.path.exists(args.tmp_dir):
        os.mkdir(args.tmp_dir, 0o777)
    try:
        pipeline = loader.load_pipeline(args)
        execute_pipeline(pipeline["steps"], args=args)
    finally:
        delete_tmp = True
        if delete_tmp:
            shutil.rmtree(args.tmp_dir, onexc=on_rm_error)

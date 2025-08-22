import argparse


def init_args() -> argparse.Namespace:
    return argparse.Namespace(
        config="pipeline.yaml",
        verbose=False,
        dry_run=True,
        tmp_dir=".",
    )

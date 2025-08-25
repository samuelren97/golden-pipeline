from threading import Thread

from goldenpipeline.InvalidConfigError import InvalidConfigError
from goldenpipeline.logger import info
from goldenpipeline.registry import STEP_REGISTRY, register_step


@register_step("parallel")
def parallel_step(
    steps: list[dict],
    is_verbose: bool,
    is_dry_run: bool,
) -> None:
    if not isinstance(steps, list):
        raise InvalidConfigError("The parallel params must be a list")

    threads: list[Thread] = []
    thread_params = {}
    count = 1
    for step in steps:
        step_name = list(step.keys())[-1]
        try:

            def run_step(c: int) -> None:
                print(f"[{count}p - {step_name}]")
                STEP_REGISTRY[step_name](
                    thread_params[str(c)],
                    is_verbose,
                    is_dry_run,
                )

            t = Thread(target=run_step, args=[count])
            thread_params[str(count)] = step[step_name]
            info(f"Starting thread for step {step_name}...")
            t.start()
            threads.append(t)

        except KeyError:
            raise KeyError(f"Step {step_name} is not a valid step")
        count += 1

    info("Waiting for parallel jobs to finish...")
    for thread in threads:
        thread.join()
    info("Parallel jobs are all done")

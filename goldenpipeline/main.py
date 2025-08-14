import loader
from registry import STEP_REGISTRY

if __name__ == "__main__":
    pipeline = loader.load_pipeline("pipeline.yaml")
    print(pipeline)
    print(STEP_REGISTRY)
    STEP_REGISTRY["checkout"]()

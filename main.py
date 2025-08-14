import loader

if __name__ == "__main__":
    pipeline = loader.load_pipeline("pipeline.yaml")
    print(pipeline)

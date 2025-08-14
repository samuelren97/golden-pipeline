pipeline_content_valid_config = """
steps:
    - checkout:
        repo: ./src
"""

pipeline_content_steps_missing = """
test:
    one: hey
"""

pipeline_content_steps_not_list = """
steps:
    checkout: hey
"""

pipeline_content_unknown_step = """
steps:
    - oh-yeah:
        parameter: "ok?"
"""

# YAML-Driven CI/CD Pipeline

A lightweight, modular and local CI/CD pipeline runner written in Python.  
Pipelines are defined in **YAML** and executed step by step by a pluggable system of registered steps.

## Features
- Define pipelines in simple YAML files.
- Step-based execution system using a registry (`@register_step` decorator).
- Modular step implementations (e.g., `checkout`, `transform`, `copy`).
- Clear logging of step execution.
- CLI options (`--config`, `--verbose`, `--dry-run`).
- Extensible architecture: just drop new step files into `steps/` to add functionality.
- Variables & templating
- Parallel execution
- Simple Docker compose integration

---

## Example Pipeline
```yaml
# pipeline.yaml

steps:
  # Prepare workspace
  - shell:
      command: "rm -rf ./build && mkdir build"
      stop_on_error: true
      cwd: ${project_root}

  # Fetch and update repo
  - shell:
      command: "git fetch --all"
      stop_on_error: true
      cwd: ${project_root}

  - shell:
      command: "git checkout ${branch}"
      stop_on_error: true
      cwd: ${project_root}

  - shell:
      command: "git pull"
      stop_on_error: false
      cwd: ${project_root}

  # Run tasks in parallel (tests + linting at the same time)
  - parallel:
      - shell:
          command: "echo 'Running unit tests...'"
          stop_on_error: true
          cwd: ${project_root}
      - shell:
          command: "echo 'Running linter...'"
          stop_on_error: true
          cwd: ${project_root}

  # Transform config file values
  - transform:
      file: "${project_root}/config.yaml"
      values:
        - "PORT: 8080": "PORT: 5000"

  # Copy artifacts into build directory
  - copy:
      source: "${project_root}/Dockerfile"
      dest: "./build/Dockerfile"

  # Build and start services with Docker Compose
  - docker-compose:
      file: docker-compose.yml
      build: true

vars:
  project_root: "./my-app"
  branch: "main"
```

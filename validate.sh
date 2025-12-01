#!/bin/bash

black .
isort .
flake8 --exclude ./.venv/

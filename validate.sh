#!/bin/bash

black .
flake8 --exclude ./.venv/
isort .
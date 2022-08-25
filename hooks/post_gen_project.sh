#!/bin/bash

python3.9 -m venv .venv
.venv/bin/pip install -U setuptools pip wheel
.venv/bin/pip install -e .
{% if cookiecutter.local_model_path %}
.venv/bin/pip install -e ../{{cookiecutter.local_model_path}}
{% endif %}
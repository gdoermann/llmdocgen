#!/bin/bash

# Script to build and distribute the package to PyPi
# You may want to bump the version number before running this script
# Example Version Bump:
# bumpver update --minor

# This should be run inside the virtual environment

# Usage: ./distribute.sh

python -m build && \
twine upload -r pypi dist/*

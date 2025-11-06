#!/bin/bash
set -ex

# install wheel from build.sh
pip install dist/scikit_misc*.whl

# clean up dist folder for building tests
rm -rf dist

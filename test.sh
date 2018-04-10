#!/usr/bin/env bash
export PYTHONAPTH="$(pwd)"
cd test
python -m unittest discover -v --pattern=*.py
cd ..

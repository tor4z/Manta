#! /usr/bin/bash
export PYTHONAPTH="$PYTHONAPTH:$(pwd)"
cd test 
python -m unittest discover --pattern=*.py -v
cd ..
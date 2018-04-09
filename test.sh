#! /usr/bin/bash
cd test 
export PYTHONAPTH="$PYTHONAPTH:${cwd}"
python -m unittest discover --pattern=*.py -v
cd ..
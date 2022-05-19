#! /bin/zsh

source ./condasetup.sh
echo ./getlatest.sh
./getlatest.sh

python append.py
python build.py













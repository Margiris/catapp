#!/bin/bash

cd ~/catpic
git checkout dev
git pull
source ./venv/bin/activate
pip install -r ./requirements.txt
python server.py
#!/bin/bash

cd ~/catpic

git checkout dev
git pull

cp ./scripts/catpic_server_start.sh ~/.termux/tasker/

source ./venv/bin/activate

pip install -r ./requirements.txt

python ./server.py

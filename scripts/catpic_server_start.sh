#!/bin/bash

cd ~/catpic

git checkout dev
git pull

cp ./scripts/catpic_server_start.sh ~/.termux/tasker/

source ./venv/bin/activate
if [$(which python) = "/data/data/com.termux/files/home/catpic/venv/bin/python"] then
    pip install -r ./requirements.txt
else
    echo $(which python)
fi

python ./server.py

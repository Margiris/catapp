#!/bin/bash

# go to project dir
cd ~/catpic

# update dev branch
git checkout dev
git pull

# if scripts differ we assume that it was updated and copy new script in place of older and exec it 
cmp ~/.termux/tasker/catpic_server_start.sh ./scripts/catpic_server_start.sh
|| cp ./scripts/catpic_server_start.sh ~/.termux/tasker/
&& exec ~/.termux/tasker/catpic_server_start.sh

which python
source ./venv/bin/activate
which python

if [$(which python) = "/data/data/com.termux/files/home/catpic/venv/bin/python"] then
    pip install -r ./requirements.txt
else
    echo $(which python)
fi

python ./server.py

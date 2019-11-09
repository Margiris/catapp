#!/bin/bash
cat ~/.termux/tasker/catpic_server_start.sh
# go to project dir
cd ~/catpic

#  drop any changes
git stash save --keep-index
git stash drop

# update dev branch
git checkout dev
git pull

# if scripts differ we assume that it was updated
if cmp -s ~/.termux/tasker/catpic_server_start.sh ./scripts/catpic_server_start.sh
then
    # copy new script in place of older one then exec it
    cp ./scripts/catpic_server_start.sh ~/.termux/tasker/
    exec ~/.termux/tasker/catpic_server_start.sh
fi

# activate virtual environment
source ./venv/bin/activate

# if virtual environment activation successful update dependencies and run server
if [ $(which python) = "/data/data/com.termux/files/home/catpic/venv/bin/python" ]
then
    pip install -r ./requirements.txt
    python ./server.py
else
    echo $(which python)
fi

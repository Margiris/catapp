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
    # copy new script in place of older one, then chmod (?) and exec it
    cp ./scripts/catpic_server_start.sh ~/.termux/tasker/
    # chmod 700 ~/.termux/tasker/catpic_server_start.sh
    exec ~/.termux/tasker/catpic_server_start.sh
fi

which python
# activate virtual environment
source ./venv/bin/activate
which python

if [ $(which python) = "/data/data/com.termux/files/home/catpic/venv/bin/python" ]
then
    pip install -r ./requirements.txt
else
    echo $(which python)
fi

python ./server.py

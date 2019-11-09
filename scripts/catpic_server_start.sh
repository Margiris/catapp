#!/bin/bash

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

# update dependencies
pip install -r ./requirements.txt

# kill any processes that might be occupying 8080 port
kill $(netstat -ltnp | grep ':8080' | awk '{ print $7 }' | sed 's/[^0-9]*//g')

#  run server
python ./server.py

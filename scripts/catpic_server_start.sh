#!/bin/bash

# go to project dir
cd ~/catpic

#  drop any changes
echo 'droping any changes...'
git stash save --keep-index
git stash drop

# update dev branch
echo 'updating dev branch...'
git checkout dev
git pull

# if scripts differ we assume that it was updated
echo 'checking for a new script version...'
if cmp -s ~/.termux/tasker/catpic_server_start.sh ./scripts/catpic_server_start.sh;
then
    echo 'no new version found, continuing'
else
    # copy new script in place of older one then exec it
    echo 'found new version, updating...'
    cp ./scripts/catpic_server_start.sh ~/.termux/tasker/catpic_server_start.sh
    echo 'restarting script...'
    exec ~/.termux/tasker/catpic_server_start.sh
fi

# activate virtual environment
echo 'activating virtual environment...'
source ./venv/bin/activate

# update dependencies
echo 'updating dependencies...'
pip install -r ./requirements.txt

# kill any processes that might be occupying 8080 port
echo 'freeing up required port...'
kill $(netstat -ltnp | grep ':8080' | awk '{ print $7 }' | sed 's/[^0-9]*//g')

#  run server
python ./server.py

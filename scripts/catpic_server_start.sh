# make sure to run as root with sudo !

# set default home path
export HOME=/data/data/com.termux/files/home

# setup variables
green_text='\e[0;32m%s\n\e[m'
red_text='\e[0;31m%s\n\e[m'

# go to project dir
cd ~/catpic

#  drop any changes
printf $green_text 'Droping any changes...'
git stash save --keep-index
git stash drop

# update dev branch
printf $green_text 'Updating dev branch...'
git checkout master
git pull

# if scripts differ we assume that it was updated
printf $green_text 'Checking for a new version...'
if cmp -s ~/tasker/catpic_server_start.sh ./scripts/catpic_server_start.sh && cmp -s ~/tasker/catpic_server_setup.sh ./scripts/catpic_server_setup.sh;
then
    printf $green_text 'No new version found, continuing'
else
    # copy new script in place of older one then exec it
    printf $green_text 'Found new version, updating...'
    mkdir /data/data/com.termux/files/home/tasker > NUL 2>&1
    cp ./scripts/catpic_server_start.sh ~/tasker/catpic_server_start.sh
    cp ./scripts/catpic_server_setup.sh ~/tasker/catpic_server_setup.sh
    sudo chmod 700 /data/data/com.termux/files/home/tasker/catpic_server_start.sh
    sudo chmod 700 /data/data/com.termux/files/home/tasker/catpic_server_start.sh
    printf $green_text 'Restarting script...'
    exec ~/tasker/catpic_server_start.sh
fi

# activate virtual environment
printf $green_text 'Activating virtual environment...'
source ./venv/bin/activate

# check if virtual environment activation successful
if [ $(which python) = "/data/data/com.termux/files/home/catpic/venv/bin/python" ]
then
    # update dependencies
    printf $green_text 'Updating dependencies...'
    pip install -r ./requirements.txt
    
    # kill any processes that might be occupying 8080 port
    printf $green_text 'Freeing up required port...'
    kill $(netstat -ltnp | grep ':80' | awk '{ print $7 }' | sed 's/[^0-9]*//g')
    
    #  run server
    printf $green_text 'Starting...'
    python ./server.py
else
    printf $red_text 'Virtual environment activation failed, current python executable:'
    printf $red_text $(which python)
    printf $red_text 'Please restart.'
fi

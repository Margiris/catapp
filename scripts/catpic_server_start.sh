# setup variables
green_text = '\e[0;32m'

# go to project dir
cd ~/catpic

#  drop any changes
printf $green_text 'Droping any changes...\n'
git stash save --keep-index
git stash drop

# update dev branch
printf $green_text 'Updating dev branch...\n'
git checkout dev
git pull

# if scripts differ we assume that it was updated
printf $green_text 'Checking for a new script version...\n'
if cmp -s ~/.termux/tasker/catpic_server_start.sh ./scripts/catpic_server_start.sh;
then
    printf $green_text 'No new version found, continuing\n'
else
    # copy new script in place of older one then exec it
    printf $green_text 'Found new version, updating...\n'
    cp ./scripts/catpic_server_start.sh ~/.termux/tasker/catpic_server_start.sh
    printf $green_text 'Restarting script...\n'
    exec ~/.termux/tasker/catpic_server_start.sh
fi

# activate virtual environment
printf $green_text 'Activating virtual environment...\n'
source ./venv/bin/activate

# update dependencies
printf $green_text 'Updating dependencies...\n'
pip install -r ./requirements.txt

# kill any processes that might be occupying 8080 port
printf $green_text 'Freeing up required port...\n'
kill $(netstat -ltnp | grep ':8080' | awk '{ print $7 }' | sed 's/[^0-9]*//g')

#  run server
python ./server.py

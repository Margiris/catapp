# go to project dir
cd ~/catpic

#  drop any changes
printf '\n\nDroping any changes...\n'
git stash save --keep-index
git stash drop

# update dev branch
printf '\n\nUpdating dev branch...\n'
git checkout dev
git pull

# if scripts differ we assume that it was updated
printf '\n\nChecking for a new script version...\n'
if cmp -s ~/.termux/tasker/catpic_server_start.sh ./scripts/catpic_server_start.sh;
then
    printf '\n\nNo new version found, continuing\n'
else
    # copy new script in place of older one then exec it
    printf '\n\nFound new version, updating...\n'
    cp ./scripts/catpic_server_start.sh ~/.termux/tasker/catpic_server_start.sh
    printf '\n\nRestarting script...\n'
    exec ~/.termux/tasker/catpic_server_start.sh
fi

# activate virtual environment
printf '\n\nActivating virtual environment...\n'
source ./venv/bin/activate

# update dependencies
printf '\n\nUpdating dependencies...\n'
pip install -r ./requirements.txt

# kill any processes that might be occupying 8080 port
printf '\n\nFreeing up required port...\n'
kill $(netstat -ltnp | grep ':8080' | awk '{ print $7 }' | sed 's/[^0-9]*//g')

#  run server
python ./server.py

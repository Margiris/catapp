# setup variables
green_text='\e[0;32m%s\n\e[m'

# install dependencies
printf $green_text 'Installing dependencies...'
pkg install git ncurses-utils python

# download and setup sudo
printf $green_text 'Setting up sudo...'
rm -fR ~/termux-sudo
git clone https://gitlab.com/st42/termux-sudo ~/termux-sudo
cd ~/termux-sudo
cat sudo > /data/data/com.termux/files/usr/bin/sudo
chmod 700 /data/data/com.termux/files/usr/bin/sudo
cd ..
rm -fR ~/termux-sudo

# download catpic
printf $green_text 'Downloading project...'
rm -fR ~/catpic
git clone https://github.com/Margiris/catpic ~/catpic
git checkout dev

# go to project dir
cd ~/catpic
cp /sdcard/secrets.py ./

# setup python virtual environment
printf $green_text 'Setting up python virtual environment...'
rm -fR ./venv
python -m venv ./venv

# copy server startup script
printf $green_text 'Creating script to start the server...'
cp ./scripts/catpic_server_start.sh ~/tasker/catpic_server_start.sh 

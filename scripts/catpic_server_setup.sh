# setup variables
green_text='\e[0;32m%s\n\e[m'
red_text='\e[0;31m%s\n\e[m'

# install dependencies
printf $green_text 'Installing dependencies...'
pkg install git ncurses-utils python

# download and setup sudo
printf $green_text 'Setting up sudo...'
git clone https://gitlab.com/st42/termux-sudo ~/termux-sudo
cd ~/termux-sudo
cat sudo > /data/data/com.termux/files/usr/bin/sudo
chmod 700 /data/data/com.termux/files/usr/bin/sudo
cd ..
rm -R ~/termux-sudo

# download catpic
printf $green_text 'Downloading project...'
git clone https://github.com/Margiris/catpic ~/catpic
git checkout dev

# go to project dir
cd ~/catpic
cp /sdcard/secrets.py ./

# setup python virtual environment
printf $green_text 'Setting up python virtual environment...'
rm -R ./venv
python -m venv ./venv

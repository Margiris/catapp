# setup variables
green_text='\e[0;32m%s\n\e[m'
red_text='\e[0;31m%s\n\e[m'

# install dependencies
pkg install git
pkg install ncurses-utils
pkg install python

# download and setup sudo
git clone https://gitlab.com/st42/termux-sudo ~/termux-sudo
cd ~/termux-sudo
cat sudo > /data/data/com.termux/files/usr/bin/sudo
chmod 700 /data/data/com.termux/files/usr/bin/sudo
cd ..
rm -R ~/termux-sudo

# download catpic
git clone https://github.com/Margiris/catpic ~/catpic
git checkout dev

# go to project dir
cd ~/catpic
cp /sdcard/secrets.py ./

rm -R ./venv
python -m venv ./venv

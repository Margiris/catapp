# setup variables
green_text='\e[0;32m%s\n\e[m'

# install dependencies
printf $green_text 'Installing dependencies...'
pkg install git ncurses-utils python libjpeg-turbo

# download and setup sudo
printf $green_text 'Setting up sudo...'
rm -fR ~/termux-sudo
git clone https://gitlab.com/st42/termux-sudo.git ~/termux-sudo

cat ~/termux-sudo/sudo > /data/data/com.termux/files/usr/bin/sudo
chmod 700 /data/data/com.termux/files/usr/bin/sudo

rm -fR ~/termux-sudo

# download catpic
printf $green_text 'Downloading project...'
sudo rm -fR ~/catpic
git clone https://github.com/Margiris/catpic.git ~/catpic
cd ~/catpic
git checkout dev

# copy and change persissions for secrets.py
sudo cp /data/media/0/secrets.py ~/catpic/
sudo chown u0_a347:u0_a347 ~/catpic/secrets.py
sudo chmod 640 ~/catpic/secrets.py

# setup python virtual environment
printf $green_text 'Setting up python virtual environment...'
rm -fR ~/catpic/venv
python -m venv ~/catpic/venv

# copy server startup script
printf $green_text 'Creating script to start the server...'
cp ~/catpic/scripts/catpic_server_start.sh ~/tasker/catpic_server_start.sh
chmod 700 ~/tasker/catpic_server_start.sh

# activate virtual environment
printf $green_text 'Activating virtual environment...'
source ./venv/bin/activate

# check if virtual environment activation successful
if [ $(which python) = "/data/data/com.termux/files/home/catpic/venv/bin/python" ]
then
    # isntall Pillow dependency since it needs special treatment
    printf $green_text 'Installing Pillow dependency...'
    LDFLAGS="-L/system/lib/" CFLAGS="-I/data/data/com.termux/files/usr/include/" pip install Pillow
fi

printf $green_text 'Done.'

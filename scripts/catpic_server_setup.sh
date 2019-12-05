# copy itself to required dir and restart
if [ $(pwd) != '/data/data/com.termux/files/home/tasker' ];
then
    mv ./catpic_server_setup.sh /data/data/com.termux/files/home/
    mkdir /data/data/com.termux/files/home/tasker > NUL 2>&1
    mv /data/data/com.termux/files/home/catpic_server_setup.sh /data/data/com.termux/files/home/tasker/
    exec ~/tasker/catpic_server_setup.sh
fi

# setup variables
green_text='\e[0;32m%s\n\e[m'

# update system
apt update
apt upgrade
# install dependencies separately to work around missing packages
printf $green_text 'Installing dependencies...'
for i in git ncurses-utils python libjpeg-turbo clang ndk-root libcrypt zlib; do
  apt install $i
done

# download and setup sudo
printf $green_text 'Setting up sudo...'
rm -fR ~/termux-sudo
git clone https://gitlab.com/st42/termux-sudo.git ~/termux-sudo

cat ~/termux-sudo/sudo > /data/data/com.termux/files/usr/bin/sudo
chmod 700 /data/data/com.termux/files/usr/bin/sudo

rm -fR ~/termux-sudo

# wait for root permission if needed
printf $green_text 'Waiting for root permission...'
sudo ls > NUL
# if [ $? -ne 0 ]; then
#     read
# fi

# download catpic
printf $green_text 'Downloading project...'
sudo rm -fR ~/catpic
git clone https://github.com/Margiris/catpic.git ~/catpic
cd ~/catpic
git checkout master

# copy and change persissions for secrets.py
sudo cp /data/media/0/secrets.py ~/catpic/
sudo chmod 600 ~/catpic/secrets.py

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
    # install Pillow dependency since it needs special treatment
    printf $green_text 'Installing Pillow dependency...'
    export LDFLAGS='-L/data/data/com.termux/files/usr/lib/'
    export CFLAGS='-I/data/data/com.termux/files/usr/include/'
    pip install Pillow
else
    printf $red_text 'Virtual environment activation failed, current python executable:'
    printf $red_text $(which python)
    printf $red_text 'Please restart.'
fi

printf $green_text 'Done.'

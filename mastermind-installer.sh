#!/bin/bash
cd
echo 'Downloading repository...'
wget https://github.com/rafael31101995/Mastermind-Game/archive/master.zip
echo 'unzip repository'
unzip ~/master.zip
echo 'removing repository .zip'
rm -r ~/master.zip
echo 'trying to install pip virtualenv'
pip install virtualenv
echo 'creating venv'
virtualenv -p python3 ~/Mastermind-Game-master/venv
echo 'activate venv'
source ~/Mastermind-Game-master/venv/bin/activate
echo 'installing requirements'
pip install -r ~/Mastermind-Game-master/requirements.txt


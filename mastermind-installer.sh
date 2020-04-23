#!/bin/bash

$(wget https://github.com/rafael31101995/Mastermind-Game/archive/master.zip)
$(unzip master.zip)
$(pip install virtualenv)
$(virtualenv -p python3 master/venv)
$(source master/venv/bin/activate)
$(pip install -r master/requirements.txt)
$(deactivate)

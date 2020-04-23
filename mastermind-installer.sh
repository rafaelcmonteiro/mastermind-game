#!/bin/bash

$(wget https://github.com/rafael31101995/Mastermind-Game/archive/master.zip)
$(unzip master.zip)
$(pip install virtualenv)
$(virtualenv -p python3 Mastermind-Game-master/venv)
$(source Mastermind-Game-master/venv/bin/activate)
$(pip install -r Mastermind-Game-master/requirements.txt)
$(deactivate)

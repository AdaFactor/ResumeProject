#!/bin/zsh
#terminator --new-tab
source ./.env/bin/activate
python3 ./resumeSite/manage.py runserver

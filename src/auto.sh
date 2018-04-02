#!/bin/zsh
#terminator --new-tab
source ./.env/bin/activate
python ./resumeSite/manage.py runserver

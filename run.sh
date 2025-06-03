#! /bin/bash

source ./venv/bin/activate

if [[ $? != 0 ]]; then
	./venv-prepare.sh
	
	source ./venv/bin/activate
fi

python3 manage.py runserver
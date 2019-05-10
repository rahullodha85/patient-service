#!/bin/bash

echo "creating containers"
docker-compose up -d

if [ ! -d "$DIRECTORY" ]; then
  echo creating virtual environment
  mkdir .venv
  python3 -m venv .venv
fi
echo "activating virtual environment"
source .venv/bin/activate

echo "installing dependencies"
pip install -r requirements.txt

echo "Create DB schema"
python mainsite/manage.py makemigrations
python mainsite/manage.py migrate
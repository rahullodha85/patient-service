#!/bin/bash
DIRECTORY=$1
echo "creating containers"
docker-compose up -d

if [ ! -d "$DIRECTORY" ]; then
  echo creating virtual environment
  python3 -m venv ../.venv_django
fi
echo "activating virtual environment"
source ../.venv_django/bin/activate

echo "installing dependencies"
pip install -r requirements.txt

echo "Create DB schema"
python mainsite/manage.py makemigrations
python mainsite/manage.py migrate
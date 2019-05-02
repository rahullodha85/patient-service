# Setup

### Setup python3 virtual environment

1. Create .venv directory at this project's root level
2. Run following command to setup virtual environment with python3 `python3 -m venv .venv`
3. Activate this virtual environment by running following command
`source .venv/bin/activate`
4. Check your python and pip versions for your virtual environment.
5. Install all dependencies. `pip install -r requirements.txt`

### How to run locally

1. Install mysql workbench. https://www.mysql.com/products/workbench/
2. Docker pull mariadb from docker hub
3. Run `docker run --name test-mariadb -e MYSQL_ROOT_PASSWORD=test123 -d -p 3306:3306 mariadb` to run mariadb in a docker container.
4. Connect to mariadb and Create a new database named `medicalclinic`.
4. Navigate to mainsite directory and run `python manage.py makemigrations` and `python manage.py migrate`
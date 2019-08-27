import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from flask_app.app.config import config_vals

db = SQLAlchemy()

def create_app(config_name):
    application = Flask(__name__, instance_relative_config=True)
    application.config.from_object(config_vals[config_name])
    # app.config.from_pyfile('config.py')
    db.init_app(application)
    migrate = Migrate(application, db)
    from flask_app.app.models.patient import patient
    return application


config_name = os.getenv('ENV')
app = create_app(config_name)

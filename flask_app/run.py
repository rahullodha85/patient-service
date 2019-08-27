from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy



# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
from app import app
from app.routes.patient import patient_controller

app.register_blueprint(patient_controller, url_prefix='/patient')

@app.route('/')
def index():
    return 'Home Page!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')

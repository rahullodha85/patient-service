from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy



# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
from flask_app.app import app

# app.register_blueprint(user_controller, url_prefix='/user')


@app.route('/')
def index():
    return 'Home Page!'


if __name__ == '__main__':
    app.run()

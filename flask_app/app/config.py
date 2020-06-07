class Config(object):
    """
    Default configurations
    """
    SECRET_KEY = 'my_secret'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    """
    Local dev config
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:test123@localhost:3306/medicalclinic'
    AUTH_URL = 'http://localhost:8000'


class ProdConfig(Config):
    """
    production config
    """


config_vals = {
    'dev': DevConfig,
    'prod': ProdConfig
}

import os

class Config():
    SECRET_KEY = 'Free'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sandys:Stanford1*@localhost/donation'
    DEBUG = True


class ProdConfig(Config):
    pass

class TestConfig(Config):
    pass


config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}
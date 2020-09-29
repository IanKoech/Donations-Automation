import os

class Config():
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sandys:Stanford1*@localhost/donations'

class ProdConfig(Config):
    pass
class TestConfig(Config):
    pass


config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}
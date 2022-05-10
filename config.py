## Configuration files 
import os

class Config:
    password = os.environ.get('SQL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:{}@localhost/pitchme'.format(password)
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

class TestConfig(Config):
    password = os.environ.get('SQL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:{}@localhost/pitchme_test'.format(password)
    pass

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}

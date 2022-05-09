## Configuration files 
import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:{password}@localhost/pitchme'
    print(SQLALCHEMY_DATABASE_URI)
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

class TestConfig(Config):
    password = os.environ.get('SQL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:{password}@localhost/pitchme_test'
    print(SQLALCHEMY_DATABASE_URI)
    pass

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}

## Configuration files 
import os

class Config:
    password = os.environ.get('SQL_PASSWORD')
    #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:{}@localhost/pitchme'.format(password)
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:GenZ|0420@localhost/pitchme'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
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

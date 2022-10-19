import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Base config"""
    SECRET_KEY = os.environ['SECRET_KEY']
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True

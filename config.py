import datetime
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    SQL_CLOUD_PASSWORD = os.environ.get('SQL_CLOUD_PASSWORD')
    SQL_LOCAL_PASSWORD = os.environ.get('SQL_LOCAL_PASSWORD')
    JSON_SORT_KEYS=True 
    JWT_TOKEN_LOCATION = ["cookies"]
    JWT_COOKIE_CSRF_PROTECT=True
    JWT_CSRF_IN_COOKIES = False
    JWT_ACCESS_CSRF_HEADER_NAME = "XCSRFTOKEN"
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=100)
    JWT_COOKIE_SECURE = True
    #JWT_COOKIE_DOMAIN = [".localhost"]

class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:{}@35.193.137.245:3306/swpit'.format(Config.SQL_CLOUD_PASSWORD)
    JWT_SECRET_KEY = Config.SQL_CLOUD_PASSWORD
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:{}@localhost:3306/swpit'.format(Config.SQL_LOCAL_PASSWORD)
    JWT_SECRET_KEY = Config.SQL_LOCAL_PASSWORD
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #JWT_ACCESS_TOKEN_EXPIRES = False

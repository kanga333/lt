import os

class DevConfig:
    __user = os.getenv('DB_USER', 'root')
    __password = os.getenv('DB_PASSWORD', '')
    __host = os.getenv('DB_HOST', 'localhost')
    __db_name = os.getenv('DB_NAME', 'lt')
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{__user}:{__password}@{__host}/{__db_name}"
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SECRET_KEY = b'\xb4B\x9f\tXd\xd9\x07\xa1\xdf\xd7\x0c\x80\xe9\xf4&'

Config = DevConfig

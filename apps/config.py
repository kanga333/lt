class DevConfig:
    __user = "root"
    __password = ""
    __host = "localhost"
    __db_name = "lt"
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{__user}:{__password}@{__host}/{__db_name}"
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SECRET_KEY = b'\xb4B\x9f\tXd\xd9\x07\xa1\xdf\xd7\x0c\x80\xe9\xf4&'

Config = DevConfig

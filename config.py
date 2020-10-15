class Config(object):
    SECRET_KEY = 'emma'


class DevelConfig(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./basedades/enercomm.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'emma'
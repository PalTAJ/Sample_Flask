import os
import datetime
from .app import app

class BaseConfig:


    JWT_EXPIRATION_DELTA = datetime.timedelta(days=25)


    app.config['MONGODB_SETTINGS'] = {
        'db': 'sample1', #sample2
        'host': 'localhost',
        'port': 27017#27019
        }


class ProductionConfig(BaseConfig):
    DEBUG = False
    Testing = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    TESTING = True

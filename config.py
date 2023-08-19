import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://gogo:IvhCW21qkB278n6ReG9Ri7erdnl8Y6rz@dpg-cjg2kr41ja0c739p5udg-a.singapore-postgres.render.com/aiai'
class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://text:dOYOKrAUebPz3oNCaOaVAdVEIR5DmX5r@dpg-cjbiobfdb61s7395gkcg-a.singapore-postgres.render.com/text_k3w9'
class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
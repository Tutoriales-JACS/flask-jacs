

class Config: 
    SECRET_KEY = 'AD1;2,3F2c1-h*_?nF!S.!345F%D&·A$'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #SQLALCHEMY_ENGINE_OPTIONS = {'pool_recycle': 280, 'pool_timeout': 100, 'pool_pre_ping': True}

class DevelopConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./test.db'
    

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:123456@127.0.0.1:5432/agrosechura'

config = {
    'develop': DevelopConfig,
    'production': ProductionConfig
}
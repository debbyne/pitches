import os
class Config:
     SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:Access@localhost/pitches'
     @staticmethod
     def init_app(app):
        pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig

}
import os
class Config:
     SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:Access@localhost/pitches'
     SQLALCHEMY_TRACK_MODIFICATIONS = False
     UPLOADED_PHOTOS_DEST = 'app/static/image'
     SIMPLEMDE_JS_IIFE = True
     SIMPLEMDE_USE_CDN = True

     MAIL_SERVER = 'smtp.googlemail.com'
     MAIL_PORT = 587
     MAIL_USE_TLS = True
     MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
     MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


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
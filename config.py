import os
class Config:
     SQLALCHEMY_TRACK_MODIFICATIONS = False
     UPLOADED_PHOTOS_DEST = 'app/static/image'
     MAIL_SERVER = 'smtp.googlemail.com'
     MAIL_PORT = 587
     MAIL_USE_TLS = True
     MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
     MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
     SECRET_KEY = '56'


     @staticmethod
     def init_app(app):
        pass


class ProdConfig(Config):
     SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URI')


class DevConfig(Config):
     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/pitches'
     DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig

}

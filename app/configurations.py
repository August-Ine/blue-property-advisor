import os
#base directory for sqlalchemy db
basedir = os.path.abspath(os.path.dirname(__file__)) 

class Config():
     #set to false to use less memory since signals for object changes are not needed
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #additional method to allow apps to define custom configurations, empty for now
    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    DEBUG = True
    #get the path for sqlalchemy db from environ variable or use predifined path if it's none
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL','sqlite:///' + os.path.join(basedir,'data-dev.sqlite'))
    

config = {
    'development' : DevConfig
}
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

#import config dictionary from configurations
from .configurations import config

#create instance of class Bootstrap to make it available to all templates defined by routes from app
bootstrap = Bootstrap()

#instance of class SQLAlchemy
db = SQLAlchemy()

def create_app(config_name):
    #create instance of flask app
    app = Flask(__name__)

    #fetch configuration settings from config dict
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    #associate the bootstrap class instance with the app
    bootstrap.init_app(app)

    #assoc db instance with the app
    db.init_app(app)

    #import the main blueprint from main subpackage and register with the app
    from .main import main as mainbp
    app.register_blueprint(mainbp)
    return app
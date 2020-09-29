from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_blueprint import Blueprint
from flask_bootstrap import Bootstrap


#instantiating flask extensions
db = SQLAlchemy()
bootstrap =Bootstrap()



def create_app(config_name):

    app = Flask(__name__)
    
    
    #setting up configurations
    app.config.from_object(config_options[config_name])
    # config_options[config_name].init_app(app)

    #Initializing flask extensions
    db.init_app(app)
    bootstrap.init_app(app)
    # blueprint.init_app(app)

    #register the charity blueprint
    from .charity import charity as charity_blueprint
    app.register_blueprint(charity_blueprint)

    return app






















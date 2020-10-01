from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_blueprint import Blueprint
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_login import LoginManager

#instantiating flask extensions
db = SQLAlchemy()
bootstrap =Bootstrap()
mail = Mail()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'



def create_app(config_name):

    app = Flask(__name__)

    app.config['TESTING'] = False
    
    
    #setting up configurations
    app.config.from_object(config_options[config_name])
    # config_options[config_name].init_app(app)

    #Initializing flask extensions
    db.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)
    # blueprint.init_app(app)

    #register the charity blueprint
    from .charity import charity as charity_blueprint
    app.register_blueprint(charity_blueprint)

    #register donor blueprint
    from .donor import donor as donor_blueprint
    app.register_blueprint(donor_blueprint)

    #registering the auth blueprint
    from .Auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app






















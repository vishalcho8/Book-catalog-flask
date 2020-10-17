#app/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.login_view = 'authentication.do_the_login'
login_manager.session_protection = 'strong'
bcrypt = Bcrypt()

#This fucntion can be called as application factory because we are creating flask app on the fly with desired config.
def create_app(config_type): #dev, test or prod
    flask_inst = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'app', 'config', config_type + '.py')
    #configuration = C:\\Python\\Book_Catalog\\config\\dev.py

    flask_inst.config.from_pyfile(configuration)
    db.init_app(flask_inst) #bind database to flask app
    bootstrap.init_app(flask_inst) #initialize bootstrap
    login_manager.init_app(flask_inst)
    bcrypt.init_app(flask_inst)

    from app.catalog import main #import blueprint
    flask_inst.register_blueprint(main) #register blueprint

    from app.auth import authentication
    flask_inst.register_blueprint(authentication)

    return flask_inst


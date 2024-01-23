# __init__.py located at C:\Code\flaskProject9\yourapp\__init__.py

from flask import Flask
from yourapp.main import main as main_blueprint
from yourapp.extensions import db, login_manager
from yourapp.config import Config
from flask_migrate import Migrate

import os
from dotenv import load_dotenv
load_dotenv()

def create_app():
    app = Flask(__name__, template_folder='main/templates')
    app.config['DEBUG'] = True
    app.config.from_object(Config)

    # Initialize extensions with the app instance
    db.init_app(app)
    login_manager.init_app(app)
    Migrate(app, db)

    # from yourapp.main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

from apscheduler.schedulers.background import BackgroundScheduler
from dotenv import load_dotenv
from .extensions import db, login_manager

# Load environment variables from .env file
load_dotenv()

# Initialize database and other extensions
migrate = Migrate()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)

    # Import Config class from config module
    from .config import Config
    app.config.from_object(Config)

    # Initialize extensions with the app instance
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Import models
    from .models import User  # Assuming User model is defined in models.py

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Import routes from routes module
    from .routes import main
    app.register_blueprint(main)  # Register the blueprint

    # Initialize and configure scheduler
    scheduler = BackgroundScheduler()
    with app.app_context():
        from .tasks import daily_check
        scheduler.add_job(daily_check, 'cron', hour=6, minute=15)
        scheduler.start()

    return app

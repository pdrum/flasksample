# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Load configurations
    app.config.from_object('app.config.Config')

    # Initialize extensions
    db.init_app(app)
    Migrate(app, db)

    # Import and register models (this is key for migrations)
    from app.models import User

    # Register Blueprints (for routes)
    from app.routes.auth_routes import auth_bp
    app.register_blueprint(auth_bp)

    return app

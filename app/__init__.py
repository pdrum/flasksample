# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Load configurations
    app.config.from_object('app.config.Config')

    # Initialize extensions
    db.init_app(app)

    # Register Blueprints (for routes)
    from app.routes.hello import hello_bp
    app.register_blueprint(hello_bp)

    return app

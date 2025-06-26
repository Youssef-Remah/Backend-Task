"""
This file:

- Creates and configures a Flask application instance
- Binds SQLAlchemy to the Flask app
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()

#Factory method
def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    migrate.init_app(app, db)

    from app import models

    return app

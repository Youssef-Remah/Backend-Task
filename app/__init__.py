"""
This file:

- Creates and configures a Flask application instance
- Binds SQLAlchemy to the Flask app
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

#Factory method
def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    return app

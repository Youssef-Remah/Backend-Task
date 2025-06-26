"""
This file:

- Creates and configures a Flask application instance
- Binds SQLAlchemy to the Flask app
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate
from flasgger import Swagger
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

#Factory method
def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    migrate.init_app(app, db)

    jwt.init_app(app)

    from app import models

    from app.routes.user_routes import user_bp

    app.register_blueprint(user_bp)

    from app.routes.book_routes import book_bp
    
    app.register_blueprint(book_bp)

    swagger = Swagger(app, template_file='swagger.yaml')

    return app

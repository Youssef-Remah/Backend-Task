from app import db

"""
This entity class:

-Inherits from the base class 'db.Model'
-Represents the 'Users' table in the database
"""
class User(db.Model):
    __tablename__ = 'Users'

    id = db.Column("Id", db.Integer, primary_key=True)

    name = db.Column("Name", db.String(120), nullable=False)

    email = db.Column("Email", db.String(120), unique=True, nullable=False)

    password = db.Column("Password", db.String(255), nullable=False)

    created_at = db.Column("CreatedAt", db.DateTime, server_default=db.func.now())

from app import db

"""
This entity class:

-Inherits from the base class 'db.Model'
-Represents the 'Books' table in the database
"""
class Book(db.Model):
    __tablename__ = 'Books'

    id = db.Column("Id", db.Integer, primary_key=True)

    title = db.Column("Title", db.String(200), nullable=False)

    description = db.Column("Description", db.Text)

    price = db.Column("Price", db.Float, nullable=False)

    release_date = db.Column("ReleaseDate", db.Date, nullable=False)

    created_at = db.Column("CreatedAt", db.DateTime, server_default=db.func.now())

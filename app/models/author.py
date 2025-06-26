from app import db

"""
This entity class:

-Inherits from the base class 'db.Model'
-Represents the 'Authors' table in the database
"""
class Author(db.Model):
    __tablename__ = 'Authors'

    id = db.Column("Id", db.Integer, primary_key=True)

    name = db.Column("Name", db.String(120), nullable=False)

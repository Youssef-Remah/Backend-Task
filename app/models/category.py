from app import db

class Category(db.Model):
    """
    Database model representing book categories/genres

    Fields:
        id (int): Primary key
        name (str): Category name (required, max 120 chars)
    """
    __tablename__ = 'Categories'

    id = db.Column("Id", db.Integer, primary_key=True)

    name = db.Column("Name", db.String(120), nullable=False)

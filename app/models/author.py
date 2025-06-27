from app import db

class Author(db.Model):
    """
    Database model representing book authors
    
    Fields:
        id (int): Primary key
        name (str): Author's full name (required, max 120 chars)
    """
    __tablename__ = 'Authors'

    id = db.Column("Id", db.Integer, primary_key=True)

    name = db.Column("Name", db.String(120), nullable=False)

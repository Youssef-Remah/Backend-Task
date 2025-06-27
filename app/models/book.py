from app import db

class Book(db.Model):
    """
    Database model representing books in the system

    Fields:
        id (int): Primary key
        title (str): Book title (required, max 200 chars)
        description (str): Optional book summary
        price (float): Retail price (required)
        release_date (date): Publication date (required)
        created_at (datetime): When record was created (auto-set)
    """
    __tablename__ = 'Books'

    id = db.Column("Id", db.Integer, primary_key=True)

    title = db.Column("Title", db.String(200), nullable=False)

    description = db.Column("Description", db.Text)

    price = db.Column("Price", db.Float, nullable=False)

    release_date = db.Column("ReleaseDate", db.Date, nullable=False)

    created_at = db.Column("CreatedAt", db.DateTime, server_default=db.func.now())

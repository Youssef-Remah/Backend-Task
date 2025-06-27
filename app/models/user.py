from app import db

class User(db.Model):
    """
    Database model representing system users

    Fields:
        id (int): Primary key
        name (str): Full name (required, max 120 chars)
        email (str): Unique email address (required, max 120 chars)
        password (str): Hashed password (required, max 255 chars)
        created_at (datetime): Account creation timestamp (auto-set)
    """
    __tablename__ = 'Users'

    id = db.Column("Id", db.Integer, primary_key=True)

    name = db.Column("Name", db.String(120), nullable=False)

    email = db.Column("Email", db.String(120), unique=True, nullable=False)

    password = db.Column("Password", db.String(255), nullable=False)

    created_at = db.Column("CreatedAt", db.DateTime, server_default=db.func.now())

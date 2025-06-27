from app import db

class BookCategory(db.Model):
    """
    Junction table for book-category many-to-many relationships

    Fields:
        book_id (int): Foreign key to Books.Id (primary key)
        category_id (int): Foreign key to Categories.Id (primary key)
    """
    __tablename__ = 'BookCategories'

    book_id = db.Column("BookId", db.Integer, db.ForeignKey('Books.Id'), primary_key=True)

    category_id = db.Column("CategoryId", db.Integer, db.ForeignKey('Categories.Id'), primary_key=True)

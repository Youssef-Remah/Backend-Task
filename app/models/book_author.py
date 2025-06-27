from app import db

class BookAuthor(db.Model):
    """
    Junction table for book-author many-to-many relationships

    Fields:
        book_id (int): Foreign key to Books.Id (primary key)
        author_id (int): Foreign key to Authors.Id (primary key)
    """
    __tablename__ = 'BookAuthors'

    book_id = db.Column("BookId", db.Integer, db.ForeignKey('Books.Id'), primary_key=True)

    author_id = db.Column("AuthorId", db.Integer, db.ForeignKey('Authors.Id'), primary_key=True)

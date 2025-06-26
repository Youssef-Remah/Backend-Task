from app import db

"""
This entity class:

-Inherits from the base class 'db.Model'
-Represents the 'BookAuthors' table in the database
"""
class BookAuthor(db.Model):
    __tablename__ = 'BookAuthors'

    book_id = db.Column("BookId", db.Integer, db.ForeignKey('Books.Id'), primary_key=True)

    author_id = db.Column("AuthorId", db.Integer, db.ForeignKey('Authors.Id'), primary_key=True)

from app import db

"""
This entity class:

-Inherits from the base class 'db.Model'
-Represents the 'BookCategories' table in the database
"""
class BookCategory(db.Model):
    __tablename__ = 'BookCategories'

    book_id = db.Column("BookId", db.Integer, db.ForeignKey('Books.Id'), primary_key=True)

    category_id = db.Column("CategoryId", db.Integer, db.ForeignKey('Categories.Id'), primary_key=True)

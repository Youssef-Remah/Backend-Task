"""
This file:

-Imports the SQLAlchemy instance 'db' to be accessed in model classes
"""
from app import db
from .user import User
from .book import Book
from .author import Author
from .category import Category
from .book_author import BookAuthor
from .book_category import BookCategory

from app import db
from app.models import Book, Author, Category, BookAuthor, BookCategory
from flask import abort

def create_book(data):
    existing_book = Book.query.filter_by(title=data["title"]).first()

    if existing_book:
        abort(400, description="A book with this title already exists")

    book = Book(
        title=data["title"],
        description=data.get("description"),
        price=data["price"],
        release_date=data["release_date"]
    )

    db.session.add(book)

    db.session.flush()

    for author_name in data["author_names"]:
        
        author = Author.query.filter_by(name=author_name).first()

        if not author:
            author = Author(name=author_name)

            db.session.add(author)

            db.session.flush()
        
        db.session.add(BookAuthor(book_id=book.id, author_id=author.id))

    for category_name in data["category_names"]:

        category = Category.query.filter_by(name=category_name).first()

        if not category:
            category = Category(name=category_name)

            db.session.add(category)
            
            db.session.flush()

        db.session.add(BookCategory(book_id=book.id, category_id=category.id))

    db.session.commit()
    
    return book


def get_book_by_id(book_id):
    
    book = Book.query.get(book_id)

    if not book:
        abort(404, description="Book not found")

    author_ids = db.session.query(BookAuthor.author_id).filter_by(book_id=book.id).all()

    authors = Author.query.filter(Author.id.in_([a[0] for a in author_ids])).all()

    author_names = [author.name for author in authors]

    
    category_ids = db.session.query(BookCategory.category_id).filter_by(book_id=book.id).all()

    categories = Category.query.filter(Category.id.in_([c[0] for c in category_ids])).all()

    category_names = [category.name for category in categories]

    return {
        "id": book.id,
        "title": book.title,
        "description": book.description,
        "price": book.price,
        "release_date": book.release_date.strftime("%Y-%m-%d"),
        "created_at": book.created_at.strftime("%Y-%m-%d %H:%M:%S") if book.created_at else None,
        "authors": author_names,
        "categories": category_names
    }

from app import db
from app.models import Book, Author, Category, BookAuthor, BookCategory
from flask import abort, make_response, jsonify

#Helpers
def _get_or_create_author(author_name):
    """Helper to find or create an author"""

    author = Author.query.filter_by(name=author_name).first()

    if not author:
        author = Author(name=author_name)

        db.session.add(author)

        db.session.flush()

    return author

def _get_or_create_category(category_name):
    """Helper to find or create a category"""

    category = Category.query.filter_by(name=category_name).first()

    if not category:
        category = Category(name=category_name)

        db.session.add(category)

        db.session.flush()

    return category

def _validate_book_data(data):
    """Validation checks"""

    if not data.get("title"):
        raise ValueError("Title is required")

    if not isinstance(data.get("price"), (int, float)):
        raise ValueError("Price must be a number")

    if not data.get("author_names"):
        raise ValueError("At least one author is required")

    if not data.get("category_names"):
        raise ValueError("At least one category is required")


def create_book(data):

    try:
        _validate_book_data(data)
        
        if Book.query.filter_by(title=data["title"]).first():
            return make_response(
                jsonify({"error": "Book title already exists", "code": 400}),
                400
            )

        book = Book(
            title=data["title"],
            description=data.get("description"),
            price=data["price"],
            release_date=data["release_date"]
        )
        db.session.add(book)
        db.session.flush()

        #Process authors
        for author_name in data["author_names"]:
            author = _get_or_create_author(author_name)
            db.session.add(BookAuthor(book_id=book.id, author_id=author.id))

        #Process categories
        for category_name in data["category_names"]:
            category = _get_or_create_category(category_name)
            db.session.add(BookCategory(book_id=book.id, category_id=category.id))

        db.session.commit()
        return make_response(
            jsonify({
                "id": book.id,
                "title": book.title,
                "description": book.description,
                "price": book.price,
                "release_date": str(book.release_date),
                "code": 201
            }),
            201
        )

    except ValueError as e:
        db.session.rollback()
        return make_response(jsonify({"error": str(e), "code": 400}), 400)
        
    except Exception as e:
        db.session.rollback()
        return make_response(
            jsonify({"error": "Book creation failed", "details": str(e), "code": 500}),
            500
        )

def get_book_by_id(book_id):

    try:
        if not isinstance(book_id, int) or book_id <= 0:
            return make_response(
                jsonify({"error": "Invalid book ID", "code": 400}),
                400
            )

        book = Book.query.get(book_id)

        if not book:
            return make_response(
                jsonify({"error": "Book not found", "code": 404}),
                404
            )

        #Get authors using inner join
        authors = Author.query.join(BookAuthor).filter(
            BookAuthor.book_id == book.id
        ).all()

        #Get categories using inner join
        categories = Category.query.join(BookCategory).filter(
            BookCategory.book_id == book.id
        ).all()

        return make_response(
            jsonify({
                "id": book.id,
                "title": book.title,
                "description": book.description,
                "price": book.price,
                "release_date": book.release_date.strftime("%Y-%m-%d"),
                "created_at": book.created_at.strftime("%Y-%m-%d %H:%M:%S") if book.created_at else None,
                "authors": [a.name for a in authors],
                "categories": [c.name for c in categories],
                "code": 200
            }),
            200
        )

    except Exception as e:
        return make_response(
            jsonify({
                "error": "Failed to fetch book",
                "details": str(e),
                "code": 500
            }),
            500
        )

def get_all_books(page, limit, price=None, release_date=None):
    query = Book.query.order_by(Book.created_at.desc())

    if price is not None:
        query = query.filter(Book.price == price)

    if release_date is not None:
        query = query.filter(Book.release_date == release_date)

    paginated_books = query.paginate(page=page, per_page=limit, error_out=False)

    books_data = []

    for book in paginated_books.items:
        author_ids = db.session.query(BookAuthor.author_id).filter_by(book_id=book.id).all()

        authors = Author.query.filter(Author.id.in_([a[0] for a in author_ids])).all()

        author_names = [author.name for author in authors]

        category_ids = db.session.query(BookCategory.category_id).filter_by(book_id=book.id).all()

        categories = Category.query.filter(Category.id.in_([c[0] for c in category_ids])).all()

        category_names = [category.name for category in categories]

        books_data.append({
            "id": book.id,
            "title": book.title,
            "description": book.description,
            "price": book.price,
            "release_date": book.release_date.strftime("%Y-%m-%d"),
            "created_at": book.created_at.strftime("%Y-%m-%d %H:%M:%S") if book.created_at else None,
            "authors": author_names,
            "categories": category_names
        })

    return {
        "total": paginated_books.total,
        "pages": paginated_books.pages,
        "current_page": paginated_books.page,
        "books": books_data
    }


def update_book(data):
    book_id = data["id"]

    book = Book.query.get(book_id)

    if not book:
        return None

    if "title" in data:
        book.title = data["title"]

    if "description" in data:
        book.description = data["description"]

    if "price" in data:
        book.price = data["price"]

    if "release_date" in data:
        book.release_date = data["release_date"]

    db.session.commit()
    
    return book
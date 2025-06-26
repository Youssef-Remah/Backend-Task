from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.schemas.book_schemas import BookCreateSchema
from app.services.book_services import create_book, get_book_by_id, get_all_books
from flask_jwt_extended import jwt_required

book_bp = Blueprint("books", __name__, url_prefix="/books")

@book_bp.route('', methods=['POST'])
@jwt_required()
def add_book():
    """
    - Creates a new book
    - Accepts book details including author and category name
    """
    schema = BookCreateSchema()
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    book = create_book(data)

    return jsonify({
        "id": book.id,
        "title": book.title,
        "description": book.description,
        "price": book.price,
        "release_date": str(book.release_date),
        "created_at": str(book.created_at)
    }), 201


@book_bp.route("/<int:book_id>", methods=["GET"])
@jwt_required()
def get_book(book_id):
    """
    - Retrieves a book by its ID
    - Returns: book data + authors + categories
    """
    book_data = get_book_by_id(book_id)

    return jsonify(book_data), 200


@book_bp.route("", methods=["GET"])
@jwt_required()
def list_books():
    """
    Returns a paginated list of books with their authors and categories.
    Query parameters:
    - page: which page to return (default = 1)
    - limit: how many books per page (default = 5)
    - price: filter books by exact price
    - release_date: filter books by exact release date (YYYY-MM-DD)
    """
    page = request.args.get("page", default=1, type=int)

    limit = request.args.get("limit", default=5, type=int)

    price = request.args.get("price", type=float)

    release_date = request.args.get("release_date")

    result = get_all_books(page, limit, price, release_date)

    return jsonify(result), 200

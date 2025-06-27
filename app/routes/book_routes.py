from flask import Blueprint, request, jsonify, make_response
from marshmallow import ValidationError
from app.schemas.book_schemas import BookCreateSchema, BookUpdateSchema
from app.services.book_services import create_book, get_book_by_id, get_all_books, update_book
from flask_jwt_extended import jwt_required

book_bp = Blueprint("books", __name__, url_prefix="/books")

@book_bp.route('', methods=['POST'])
@jwt_required()
def add_book():

    try:
        data = BookCreateSchema().load(request.json)

        return create_book(data)
        
    except ValidationError as e:
        return make_response(
            jsonify({
                "errors": e.messages,
                "code": 400
            }),
            400
        )

@book_bp.route("/<int:book_id>", methods=["GET"])
@jwt_required()
def get_book(book_id):

    return get_book_by_id(book_id)

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

@book_bp.route("", methods=["PATCH"])
@jwt_required()
def edit_book():
    """
    Updates a book's details (excluding authors and categories)
    Requires 'id' in the body
    Accepts partial update of: title, description, price, release_date
    """
    schema = BookUpdateSchema()

    try:
        data = schema.load(request.json, partial=True)

    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    book = update_book(data)

    if not book:
        return jsonify({"error": "Book not found"}), 404

    return jsonify({
        "id": book.id,
        "title": book.title,
        "description": book.description,
        "price": book.price,
        "release_date": book.release_date.strftime("%Y-%m-%d"),
        "created_at": book.created_at.strftime("%Y-%m-%d %H:%M:%S") if book.created_at else None
    }), 200

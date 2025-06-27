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
    page = request.args.get("page", default=1, type=int)
    
    limit = request.args.get("limit", default=5, type=int)
    
    price = request.args.get("price", type=float)
    
    release_date = request.args.get("release_date")
    
    return get_all_books(page, limit, price, release_date)

@book_bp.route("", methods=["PATCH"])
@jwt_required()
def edit_book():
    try:
        data = BookUpdateSchema().load(request.json, partial=True)

        return update_book(data)
    
    except ValidationError as e:
        return make_response(
            jsonify({"errors": e.messages, "code": 400}),
            400
        )

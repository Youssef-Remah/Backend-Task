from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.schemas import UserSignUpSchema
from app.services import create_user, authenticate_user

#a blue print for organizing routes related to users
user_bp = Blueprint('users', __name__, url_prefix="/users")

@user_bp.route('/signUp', methods=['POST'])
def sign_up():
    """
    This method:

    -Registers a new user and adds a new record in the Users table
    -Validates request body using the UserSignUpSchema() method

    Returns:
    - 400 status code (Bad Request) along with error messages in case of a validation error occurs
    - 201 status code (Created) along with the new user data added to the database
    """
    schema = UserSignUpSchema()

    try:
        data = schema.load(request.json)

    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    user = create_user(data)

    return jsonify({
        "id": user.id,

        "Name": user.name,

        "Email": user.email
    }), 201


@user_bp.route('/login', methods=['POST'])
def login():
    data = request.json

    email = data.get("Email")

    password = data.get("Password")

    response_data, status_code = authenticate_user(email, password)

    return jsonify(response_data), status_code

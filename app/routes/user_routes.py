from flask import Blueprint, request, jsonify, make_response
from marshmallow import ValidationError
from app.schemas.user_schemas import UserSignUpSchema, UserLoginSchema
from app.services import create_user, authenticate_user

#a blue print for organizing routes related to users
user_bp = Blueprint('users', __name__, url_prefix="/users")

@user_bp.route('/signUp', methods=['POST'])
def sign_up():

    try:
        data = UserSignUpSchema().load(request.json)

        return create_user(data)
        
    except ValidationError as e:
        return make_response(
            jsonify({"errors": e.messages, "code": 400}),
            400
        )

@user_bp.route('/login', methods=['POST'])
def login():

    try:
        data = UserLoginSchema().load(request.json)

        return authenticate_user(data['Email'], data['Password'])
        
    except ValidationError as e:
        return make_response(
            jsonify({"errors": e.messages, "code": 400}),
            400
        )

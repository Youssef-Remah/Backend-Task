from app.models.user import User
from app import db
from app.utils.security import hash_password, verify_password
from flask_jwt_extended import create_access_token
from flask import jsonify, make_response

def create_user(data):

    try:
        #Check if user email exists
        if User.query.filter_by(email=data['email']).first():
            return make_response(
                jsonify({"error": "Email already exists", "code": 400}), 
                400
            )

        user = User(
            name=data['name'],
            email=data['email'],
            password=hash_password(data['password'])
        )
        
        db.session.add(user)
        db.session.commit()
        
        return make_response(
            jsonify({
                "id": user.id,
                "name": user.name,
                "email": user.email
            }),
            201
        )

    except Exception as e:
        db.session.rollback()

        return make_response(
            jsonify({"error": "User creation failed", "details": str(e), "code": 500}),
            500
        )


def authenticate_user(email, password):
    """
    -Validates the user and generates a JWT token if valid
    
    -Returns: response_data: dict and status_code: int
    """
    user = User.query.filter_by(email=email).first()

    if not user or not verify_password(password, user.password):
        return {"error": "Invalid email or password"}, 401

    token = create_access_token(identity=user.id)

    return {
        "access_token": token,
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }
    }, 200
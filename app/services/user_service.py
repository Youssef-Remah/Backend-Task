from app.models.user import User
from app import db
from app.utils.security import hash_password, verify_password
from flask_jwt_extended import create_access_token
from flask import jsonify, make_response

def create_user(data):
    """
    Creates a new user after validation

    Args:
        data: {
            name: str,
            email: str,
            password: str
        }
    
    Returns:
        tuple: (response, status_code)
        Success (201): {id, name, email}
        Error (400): Email exists
        Error (500): Creation failed
    """
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
    Validates user credentials and generates JWT token
    
    Args:
        email: str
        password: str
    
    Returns:
        tuple: (response, status_code)
        Success (200): {access_token, user_data}
        Error (400): Missing credentials
        Error (401): Invalid credentials
        Error (500): Authentication failed
    """
    #Check if email or password are empty
    if not email or not password:
        return make_response(
            jsonify({
                "error": "Email and password required",
                "code": 400
            }),
            400
        )

    try:
        user = User.query.filter_by(email=email).first()

        if not user or not verify_password(password, user.password):
            return make_response(
                jsonify({
                    "error": "Invalid email or password", 
                    "code": 401
                }),
                401
            )

        token = create_access_token(identity=str(user.id))
        
        return make_response(
            jsonify({
                "access_token": token,
                "user": {
                    "id": user.id,
                    "name": user.name,
                    "email": user.email
                },
                "code": 200
            }),
            200
        )

    except Exception as e:
        return make_response(
            jsonify({
                "error": "Authentication failed",
                "details": str(e),
                "code": 500
            }),
            500
        )

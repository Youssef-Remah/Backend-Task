from app.models.user import User
from app import db
from app.utils.security import hash_password, verify_password
from flask_jwt_extended import create_access_token

def create_user(data):
    """
    -Accepts: an object representing the new user's data
    -Returns: User object representing the newely added user
    """
    user = User(
        name=data['Name'],

        email=data['Email'],

        password=hash_password(data['Password'])
    )

    db.session.add(user)

    db.session.commit()

    return user


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
from app.models.user import User
from app import db
from app.utils.security import hash_password

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

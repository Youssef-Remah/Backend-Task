from werkzeug.security import generate_password_hash, check_password_hash


def hash_password(password):
    """
    -Accepts: a plain text password and convert it to a hashed password
    -Returns: The hashed version of the password
    """
    return generate_password_hash(password)


def verify_password(plain_password, hashed_password):
    """
    -Accepts: plain text and hashed passwords
    -Returns: a bool indicating whether both passwords match
    """
    return check_password_hash(hashed_password, plain_password)

from marshmallow import Schema, fields, validate

class UserSignUpSchema(Schema):
    """
    Validates user registration data
    
    Fields:
        name (str): Full name (min 3 chars)
        email (str): Valid email format
        password (str): Min 6 characters
    """
    name = fields.Str(required=True, validate=validate.Length(min=3))

    email = fields.Email(required=True)

    password = fields.Str(required=True, validate=validate.Length(min=6))


class UserLoginSchema(Schema):
    """
    Validates user login credentials
    
    Fields:
        Email (str): Valid email format
        Password (str): Min 6 characters
    """
    Email = fields.Email(required=True)

    Password = fields.Str(required=True, validate=validate.Length(min=6))

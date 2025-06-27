from marshmallow import Schema, fields, validate

"""
This class:

-Used for validating request data of the user's signup
"""
class UserSignUpSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=3))

    email = fields.Email(required=True)

    password = fields.Str(required=True, validate=validate.Length(min=6))

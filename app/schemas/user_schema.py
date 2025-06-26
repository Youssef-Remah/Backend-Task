from marshmallow import Schema, fields, validate

"""
This class:

-Used for validating request data of the user's signup
"""
class UserSignUpSchema(Schema):
    Name = fields.Str(required=True, validate=validate.Length(min=3))

    Email = fields.Email(required=True)

    Password = fields.Str(required=True, validate=validate.Length(min=6))

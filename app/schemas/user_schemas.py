from marshmallow import Schema, fields, validate

class UserSignUpSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=3))

    email = fields.Email(required=True)

    password = fields.Str(required=True, validate=validate.Length(min=6))


class UserLoginSchema(Schema):
    Email = fields.Email(required=True)
    Password = fields.Str(required=True, validate=validate.Length(min=6))

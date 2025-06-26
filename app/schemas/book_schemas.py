from marshmallow import Schema, fields, validates, validates_schema, ValidationError

class BookCreateSchema(Schema):
    title = fields.Str(required=True)

    description = fields.Str()

    price = fields.Float(required=True)

    release_date = fields.Date(required=True, format="%Y-%m-%d")

    author_names = fields.List(fields.Str(), required=True)

    category_names = fields.List(fields.Str(), required=True)

    @validates_schema
    def validate_names(self, data, **kwargs):
        if not data.get("author_names"):
            raise ValidationError("At least one author is required.", field_name="author_names")
        
        if not data.get("category_names"):
            raise ValidationError("At least one category is required.", field_name="category_names")


class BookUpdateSchema(Schema):
    id = fields.Int(required=True)

    title = fields.Str()

    description = fields.Str()

    price = fields.Float()

    release_date = fields.Date(format="%Y-%m-%d")

    @validates_schema
    def validate_data(self, data, **kwargs):

        if data.get("id") is None or data["id"] <= 0:
            raise ValidationError("ID must be a positive integer.", field_name="id")

        updatable_fields = {"title", "description", "price", "release_date"}
        
        if not any(field in data for field in updatable_fields):
            raise ValidationError("At least one field to update must be provided.")
from marshmallow import Schema, fields, validates_schema, ValidationError

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
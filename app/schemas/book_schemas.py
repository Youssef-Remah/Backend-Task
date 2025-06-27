from marshmallow import Schema, fields, validates, validates_schema, ValidationError

class BookCreateSchema(Schema):
    """
    Validates book creation data

    Fields:
        title (str): Book title (required)
        description (str): Optional description
        price (float): Required price
        release_date (date): YYYY-MM-DD format (required)
        author_names (list[str]): Min 1 author required
        category_names (list[str]): Min 1 category required
    """
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
    """
    Validates book update data

    Fields:
        id (int): Positive book ID (required)
        title (str): Optional new title
        description (str): Optional new description
        price (float): Optional new price
        release_date (date): Optional new date (YYYY-MM-DD)
    """
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
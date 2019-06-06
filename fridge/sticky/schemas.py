from marshmallow import Schema, fields


class GetStickyResponseSchema(Schema):
    id = fields.Int(required=True)
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    user_id = fields.Int(required=True)

    class Meta:
        strict = True

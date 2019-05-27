from marshmallow import fields, Schema

class ReadUserSchema(Schema):
    id = fields.Int(required=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)

    class Meta:
        strict = True

class CreateUserSchema(Schema):
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True)
    passwordConfirmation = fields.Str(required=True, attribute='password_confirmation')

    class Meta:
        strict = True
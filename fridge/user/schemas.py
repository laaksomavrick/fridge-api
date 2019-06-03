from marshmallow import fields, Schema


class CreateUserResponseSchema(Schema):
    id = fields.Int(required=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)

    class Meta:
        strict = True


class CreateUserRequestSchema(Schema):
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True)
    passwordConfirmation = fields.Str(
        required=True, attribute='password_confirmation')

    class Meta:
        strict = True


class LoginUserRequestSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)

    class Meta:
        strict = True

class LoginUserResponseSchema(Schema):
    refreshToken = fields.Str(required=True, attribute='refresh_token')
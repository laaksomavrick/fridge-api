from flask import jsonify


def template(data, code=500):
    return {'message': {'errors': {'body': data}}, 'status_code': code}


USER_PASSWORD_CONFIRMATION_WRONG = template(
    ['Passwords don\'t match'], code=422)
USER_ALREADY_REGISTERED = template(['User already registered'], code=422)
USER_NOT_FOUND = template(['User not found'], code=404)
USER_BAD_PASSWORD = template(['Password is incorrect'], code=401)


class ApiError(Exception):
    status_code = 500

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_json(self):
        rv = self.message
        return jsonify(rv)

    @classmethod
    def user_already_registered(cls):
        return cls(**USER_ALREADY_REGISTERED)

    @classmethod
    def user_password_confirmation_wrong(cls):
        return cls(**USER_PASSWORD_CONFIRMATION_WRONG)

    @classmethod
    def user_not_found(cls):
        return cls(**USER_NOT_FOUND)

    @classmethod
    def user_bad_password(cls):
        return cls(**USER_BAD_PASSWORD)

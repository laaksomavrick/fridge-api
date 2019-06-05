from functools import wraps

from flask import current_app, g, redirect, request, url_for
from jwt import decode

from fridge.exceptions import ApiError


def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.get('user_id') is None:
            auth_header_value = request.headers.get('Authorization', None)
            if auth_header_value is None:
                raise ApiError.authorization_required()

            parts = auth_header_value.split()
            if len(parts) < 2:
                raise ApiError.authorization_required()

            token = parts[1]
            if token is None:
                raise ApiError.authorization_required()

            decoded = decode(
                token, current_app.config['JWT_SECRET_KEY'], algorithms=['HS256'])
            user_id = decoded['user_id']
            if user_id is None:
                raise ApiError.authorization_required()

            g.user_id = user_id

        return f(*args, **kwargs)

    return decorated_function

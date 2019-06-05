from flask import Blueprint, current_app, jsonify
from flask_apispec import marshal_with, use_kwargs
from jwt import encode

from fridge.decorators import token_required
from fridge.exceptions import ApiError
from fridge.extensions import db

from .models import User
from .schemas import (CreateUserRequestSchema, CreateUserResponseSchema,
                      LoginUserRequestSchema, LoginUserResponseSchema)

blueprint = Blueprint('user', __name__)
create_user_request_schema = CreateUserRequestSchema()
create_user_response_schema = CreateUserResponseSchema()

login_user_request_schema = LoginUserRequestSchema()
login_user_response_schema = LoginUserResponseSchema()


@blueprint.route('/api/user', methods=('POST',))
@use_kwargs(create_user_request_schema)
@marshal_with(create_user_response_schema)
def create_user(username, email, password, password_confirmation):
    if password != password_confirmation:
        raise ApiError.user_password_confirmation_wrong()

    if User.query.filter(User.username == username).first():
        raise ApiError.user_already_registered()

    user = User(username=username, email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return user

@blueprint.route('/api/user/login', methods=('POST',))
@use_kwargs(login_user_request_schema)
@marshal_with(login_user_response_schema)
def login_user(username, password):
    user = User.query.filter(User.username == username).first()
    if user is None:
        raise ApiError.user_not_found()

    ok_password = user.check_password(password)
    if ok_password is False:
        raise ApiError.user_bad_password()

    # TODO: need expiry for prod
    access_token = encode({'user_id': user.id}, current_app.config['JWT_SECRET_KEY'], algorithm='HS256')
    return {'access_token': access_token}

import logging
from flask import Blueprint, jsonify
from flask_apispec import use_kwargs, marshal_with
from fridge.exceptions import ApiError
from fridge.extensions import db
from .schemas import CreateUserSchema, ReadUserSchema
from .models import User

blueprint = Blueprint('user', __name__)
read_user_schema = ReadUserSchema()
create_user_schema = CreateUserSchema()


@blueprint.route('/api/user', methods=('POST',))
@use_kwargs(create_user_schema)
@marshal_with(read_user_schema)
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

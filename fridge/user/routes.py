import logging
from flask import Blueprint, jsonify
from flask_apispec import use_kwargs, marshal_with
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
    try:
        if password != password_confirmation:
            # Todo, error class, raise exception
            raise Exception()

        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return user
    except Exception:
        logging.exception("Something went wrong")
        return jsonify({'error': 'Something went wrong'})

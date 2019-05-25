from flask import Blueprint, jsonify

blueprint = Blueprint('users', __name__)

@blueprint.route('/api/users', methods=('GET',))
def hello_users():
    return jsonify({'hello': 'users'})

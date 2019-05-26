from flask import Blueprint, jsonify

blueprint = Blueprint('user', __name__)

@blueprint.route('/api/user', methods=('GET',))
def hello_user():
    return jsonify({'hello': 'user'})

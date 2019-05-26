from flask import Blueprint, jsonify

blueprint = Blueprint('sticky', __name__)

@blueprint.route('/api/sticky', methods=('GET',))
def hello_sticky():
    return jsonify({'hello': 'sticky'})

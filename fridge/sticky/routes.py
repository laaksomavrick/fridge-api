from flask import Blueprint, g, jsonify
from flask_apispec import marshal_with

from fridge.decorators import token_required
from fridge.exceptions import ApiError

from .models import Sticky
from .schemas import GetStickyResponseSchema

blueprint = Blueprint('sticky', __name__)

get_sticky_response_schema = GetStickyResponseSchema()

@blueprint.route('/api/sticky/<sticky_id>', methods=('GET',))
@token_required
@marshal_with(get_sticky_response_schema)
def get_sticky(sticky_id):
    sticky = Sticky.query.filter(Sticky.id == sticky_id).first()
    if sticky is None:
        raise ApiError.resource_not_found()

    if sticky.user_id is not g.user_id:
        raise ApiError.forbidden_resource()

    return sticky

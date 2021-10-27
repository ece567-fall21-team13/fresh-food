"""Customer views."""
from flask import Blueprint
from flask_apispec import use_kwargs

from freshfood.database import db
from .serializers import restaurant_schema

blueprint = Blueprint('user', __name__)


@blueprint.route('/api/restaurants/catalog', methods=('POST',))
@use_kwargs(restaurant_schema)
def list_catalog(**kwargs):
    response = []
    customer_uuid = kwargs.get('customer_uuid')
    result = db.engine.execute("SELECT * from restaurants")
    for r in result:
        row_as_dict = dict(r)
        # TODO hit the maps api for all the restaurant address and the customer's address.
        # We'll have time in mins for all restaurants for that customer_uuid
        row_as_dict['time_to_deliver'] = '10 mins'
        response.append(row_as_dict)
    return response
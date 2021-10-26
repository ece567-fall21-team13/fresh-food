"""Customer views."""
from flask import Blueprint, request
from flask_apispec import use_kwargs, marshal_with
from flask_jwt_extended import jwt_required, create_access_token, current_user
from marshmallow import RAISE
from sqlalchemy.exc import IntegrityError
from webargs.flaskparser import use_args
from freshfood.database import db
from freshfood.exceptions import InvalidUsage
from .models import Restaurants
from .serializers import restaurant_schema
from flask import Flask, request, jsonify

blueprint = Blueprint('user', __name__)


@blueprint.route('/api/restaurants/catalog', methods=('POST',))
@use_kwargs(restaurant_schema)
def list_catalog(**kwargs):
    response = []
    customer_uuid = kwargs.get('customer_uuid')
    result = db.engine.execute("SELECT * from restaurants")
    for r in result:
        row_as_dict = dict(r)
        row_as_dict['time_to_deliver'] = '10 mins'
        response.append(row_as_dict)
    return response
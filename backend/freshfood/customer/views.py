"""Customer views."""
from flask import Blueprint, request
from flask_apispec import use_kwargs, marshal_with
from flask_jwt_extended import jwt_required, create_access_token, current_user
from marshmallow import RAISE
from sqlalchemy.exc import IntegrityError
from webargs.flaskparser import use_args
from freshfood.database import db
from freshfood.exceptions import InvalidUsage
from .models import Customer
from .serializers import customer_schema, CustomerSchema
from flask import Flask, request, jsonify

blueprint = Blueprint('user', __name__)


@blueprint.route('/api/customer', methods=('POST',))
@use_kwargs(customer_schema)
@marshal_with(customer_schema)
def register_customer(email, password, **kwargs):
    # username = request.json
    try:
        customer = Customer(email, password=password, **kwargs).save()
        # customer.driver.token = create_access_token(identity=customer.driver)
    except IntegrityError:
        db.session.rollback()
        raise InvalidUsage.user_already_registered()
    return customer

@blueprint.route('/api/customer', methods=('GET',))
# @jwt_required
# @marshal_with(customer_schema)
def get_customer_address():
    user = current_user
    # Not sure about this
    # user.token = request.headers.environ['HTTP_AUTHORIZATION'].split('Token ')[1]
    return current_user


@blueprint.route('/api/user', methods=('PUT',))
# @jwt_required
@use_kwargs(customer_schema)
@marshal_with(customer_schema)
def update_user(**kwargs):
    user = current_user
    # take in consideration the password
    password = kwargs.pop('password', None)
    if password:
        user.set_password(password)
    if 'updated_at' in kwargs:
        kwargs['updated_at'] = user.created_at.replace(tzinfo=None)
    user.update(**kwargs)
    return user

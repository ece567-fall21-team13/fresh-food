# coding: utf-8

from flask import Blueprint
from flask_apispec import use_kwargs

from .serializers import order_schema
from ..extensions import db
from ..utils import generate_uuid

blueprint = Blueprint('profiles', __name__)


@blueprint.route('/api/customer/place_oder', methods=('POST',))
@use_kwargs(order_schema)
def place_order(**kwargs):
    response = []
    time_to_reach_restaurant = 0
    time_to_deliver_order_after_pickup = 0
    customer_uuid = kwargs.get('customer_uuid')
    restaurant_uuid = kwargs.get('restaurant_uuid')

    drivers_result = db.engine.execute("SELECT * from drivers")
    for r in drivers_result:
        row_as_dict = dict(r)
        response.append(row_as_dict)
    order_uuid = "odr::" + str(generate_uuid())
    # TODO Call APIS for drivers geopy
    driver_uuid = 'dri::1ea8fc98-af1d-4a6f-b942-7449b4696384';
    return {'status': 'CREATED', 'customer_id': customer_uuid, 'order_uuid': order_uuid,
            'time_delivery':time_to_reach_restaurant + time_to_deliver_order_after_pickup,
            'restaurant_uuid':restaurant_uuid}

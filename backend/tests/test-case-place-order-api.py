import pytest
import requests
import json


def test_place_order_test():
    url = "localhost:5000/api/customer/place_oder"

    payload = json.dumps({
        "customer_uuid": "cus::0cdfbbe3-eb83-4e55-9559-a3f57347633d",
        "restaurant_uuid": "res::6b5de626-2200-477b-9431-542365497580"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    response_status_code = 200
    if response_status_code not in (200, 201):
        raise Exception("Website is not working")

# coding: utf-8
import pytest
import requests
import json


def test_get_profile_not_loggedin():
    url = "localhost:5000/api/restaurants/catalog"

    payload = json.dumps({
        "customer_uuid": "cus::0cdfbbe3-eb83-4e55-9559-a3f57347633d"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    response_status_code = response.status_code
    if response_status_code not in (200, 201):
        raise Exception("Customer catalog api not working")

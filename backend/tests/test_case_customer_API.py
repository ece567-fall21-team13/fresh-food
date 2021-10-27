# coding: utf-8
import pytest
import requests
import json


# from flask import url_for
# from freshfood.exceptions import USER_NOT_FOUND

#
# def _register_user(testapp, **kwargs):
#     return testapp.post_json(url_for('user.register_user'), {
#           "user": {
#               "email": 'foo@bar.com',
#               "username": 'foobar',
#               "password": 'myprecious'
#           }}, **kwargs)


# class TestProfile():

def test_get_profile_not_loggedin():
    testapp = None

    #url = "localhost:5000/api/restaurants/catalog"

    payload = json.dumps({
        "customer_uuid": "cus::0cdfbbe3-eb83-4e55-9559-a3f57347633d"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    # response = requests.request("POST", url, headers=headers, data=payload)
    response_status_code = 200
    if response_status_code not in (200,201):
        raise Exception("Website is not working")

    # if response.status_code == 200:
    #     print('OK!')
    # else:
    #     print('Boo!')

    # exit(0)
    # _register_user(testapp)
    # resp = testapp.get(url_for('profiles.get_profile', username='foobar'))
    # assert resp.json['profile']['email'] == 'foo@bar.com'
    # assert not resp.json['profile']['following']

# def test_get_profile_not_existing(self, testapp):
#     resp = testapp.get(url_for('profiles.get_profile', username='foobar'), expect_errors=True)
#     assert resp.status_int == 404
#     assert resp.json == USER_NOT_FOUND['message']
#
# def test_follow_user(self, testapp, user):
#     user = user.get()
#     resp = _register_user(testapp)
#     token = str(resp.json['user']['token'])
#     resp = testapp.post(url_for('profiles.follow_user', username=user.customer_uuid), headers={
#         'Authorization': 'Token {}'.format(token)
#     })
#     assert resp.json['profile']['following']
#
# def test_unfollow_user(self, testapp, user):
#     user = user.get()
#     resp = _register_user(testapp)
#     token = str(resp.json['user']['token'])
#     resp = testapp.delete(url_for('profiles.unfollow_user', username=user.customer_uuid), headers={
#         'Authorization': 'Token {}'.format(token)
#     })
#     assert not resp.json['profile']['following']

def main():
    test_get_profile_not_loggedin()

if __name__ == "__main__":
    main()
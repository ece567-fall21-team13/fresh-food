# -*- coding: utf-8 -*-
"""Helper utilities and decorators."""
import uuid

# from freshfood.customer.models import Customers  # noqa


def jwt_identity(payload):
    return None #Customers.get_by_id(payload)


def identity_loader(customer):
    return None #customer.id

def generate_uuid():
    return str(uuid.uuid4())
# -*- coding: utf-8 -*-
"""User models."""

from freshfood.database import Column, Model, db
from freshfood.utils import generate_uuid


class Restaurants(Model):

    __tablename__ = 'restaurants'

    restaurant_uuid = Column(db.Text, unique=True, nullable=False, default="res"+generate_uuid(),primary_key=True)
    address = Column(db.Text, unique=True, nullable=False)

    def __init__(self, **kwargs):
        pass
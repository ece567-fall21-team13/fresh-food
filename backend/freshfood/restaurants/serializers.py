# coding: utf-8

from marshmallow import Schema, fields, pre_load, post_dump, INCLUDE


class RestaurantSchema(Schema):
    address = fields.Str()
    name = fields.Str()
    restaurant_uuid = fields.Str()
    time_to_deliver = fields.Str()

    @pre_load
    def make_user(self, data, *args, **kwargs):
        return data

    class Meta:
        # Include unknown fields in the deserialized output
        unknown = INCLUDE


restaurant_schema = RestaurantSchema()
# restaurant_schemas = RestaurantSchema(many=True)

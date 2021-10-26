from marshmallow import Schema, fields, pre_load, post_dump


class OrderSchema(Schema):
    customer_uuid = fields.Str()
    restaurant_uuid = fields.Str()

    class Meta:
        strict = True


order_schema = OrderSchema()
profile_schemas = OrderSchema(many=True)

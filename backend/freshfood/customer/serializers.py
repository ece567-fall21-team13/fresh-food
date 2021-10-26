# coding: utf-8

from marshmallow import Schema, fields, pre_load, post_dump, INCLUDE


class CustomerSchema(Schema):
    email = fields.Email()
    password = fields.Str(load_only=True)
    # bio = fields.Str()
    # createdAt = fields.DateTime(attribute='created_at', dump_only=True)
    # updatedAt = fields.DateTime(attribute='updated_at')
    # ugly hack.
    # user = fields.Nested('self', exclude=('user',), default=True, load_only=True)

    @pre_load
    def make_user(self, data, *args, **kwargs):
        # data = data['user']
        # # some of the frontends send this like an empty string and some send
        # # null
        # if not data.get('email', True):
        #     del data['email']
        # if not data.get('image', True):
        #     del data['image']
        return data

    @post_dump
    def dump_user(self, data, **kwargs):
        return {'user': data}

    class Meta:
        # Include unknown fields in the deserialized output
        unknown = INCLUDE


customer_schema = CustomerSchema()
customer_schemas = CustomerSchema(many=True)

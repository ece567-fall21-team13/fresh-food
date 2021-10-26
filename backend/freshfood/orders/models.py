from freshfood.database import (Model, db)


class Drivers(Model):
    __tablename__ = 'orders'

    def __init__(self, **kwargs):
        db.Model.__init__(self, **kwargs)

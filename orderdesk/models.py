from neobunch import NeoBunch
from properties import (
    ORDER_PROPERTIES, ORDER_ITEM_PROPERTIES,
    ADDRESS_PROPERTIES, RETURN_ADDRESS_PROPERTIES,
    DISCOUNT_PROPERTIES, ORDER_NOTE_PROPERTIES)


class BaseModel(NeoBunch):
    properties = []
    identifier = ''

    def validate(self):
        for key in self.keys():
            assert key in self.properties, \
                "%s is not a valid %s property" % (
                    self.identifier, key)


class Order(BaseModel):
    properties = ORDER_PROPERTIES
    identifier = 'order'


class OrderItem(BaseModel):
    properties = ORDER_ITEM_PROPERTIES
    identifier = 'order_item'


class Address(BaseModel):
    properties = ADDRESS_PROPERTIES
    identifier = 'address'


class ReturnAddress(BaseModel):
    properties = RETURN_ADDRESS_PROPERTIES
    identifier = 'return_address'


class Discount(BaseModel):
    properties = DISCOUNT_PROPERTIES
    identifier = 'discount'


class OrderNote(BaseModel):
    properties = ORDER_NOTE_PROPERTIES
    idenifier = 'order_note'

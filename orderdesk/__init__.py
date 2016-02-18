from client import OrderDeskClient

__version__ = '0.0.0'


def get_client(store_id=None, apikey=None):
    return OrderDeskClient(
        store_id=store_id, apikey=apikey)

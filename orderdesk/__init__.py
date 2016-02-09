from client import OrderDeskClient


def get_client(store_id=None, apikey=None):
    return OrderDeskClient(
        store_id=store_id, apikey=apikey)

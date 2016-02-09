from base import OrderDeskBaseClient


class TestClient(OrderDeskBaseClient):

    def test_connection(self):
        return self.get('test', {})


class OrderClient(OrderDeskBaseClient):
    def get_order(self, order_id):
        resource = '/orders/%s' % order_id
        return self.get(resource)

    def get_orders(self, data):
        resource = '/orders'
        return self.get(resource, data=data)

    def create_order(self, data):
        resource = '/orders'
        return self.post(resource, data=data)

    def update_order(self, order_id, data):
        resource = '/orders/%s' % order_id
        return self.put(resource, data=data)

    def delete_order(self, order_id):
        resource = '/orders/%s' % order_id
        return self.delete(resource)


class MoveOrdersClient(OrderDeskBaseClient):
    def move_orders(self, data):
        resource = '/move-orders'
        return self.post(resource, data)


class OrderHistoryClient(OrderDeskBaseClient):

    def create_order_history_item(self, order_id, data):
        resource = '/orders/%s/order-history' % order_id
        return self.post(resource, data=data)


class OrderItemClient(OrderDeskBaseClient):

    def get_order_items(self, order_id):
        resource = '/orders/%s/order-items' % order_id
        return self.get(resource)

    def get_order_item(self, order_id, order_item_id):
        resource = '/orders/%s/order-items/%s' % (
            order_id, order_item_id)
        return self.get(resource)

    def create_order_item(self, order_id, data):
        resource = '/orders/%s/order-items/%s' % order_id
        return self.post(resource, data=data)

    def update_order_item(self, order_id, order_item_id, data):
        resource = '/orders/%s/order-items/%s' % (
            order_id, order_item_id)
        return self.put(resource, data=data)

    def delete_order_item(self, order_id, order_item_id):
        resource = '/orders/%s/order-items/%s' % (
            order_id, order_item_id)
        return self.delete(resource)


class ShipmentClient(OrderDeskBaseClient):

    def get_order_shipments(self, order_id):
        resource = '/orders/%s/shipments' % order_id
        return self.get(resource)

    def get_order_shipment(self, order_id, shipment_id):
        resource = '/orders/%s/shipments/%s' % (
            order_id, shipment_id)
        return self.get(resource)

    def create_shipment(self, order_id, data):
        resource = '/orders/%s' % order_id
        return self.post(resource, data=data)

    def delete_shipment(self, order_id, shipment_id):
        resource = '/orders/%s' % order_id
        return self.delete(resource)


class InventoryClient(OrderDeskBaseClient):

    def get_inventory_items(self):
        resource = '/inventory-items'
        return self.get(resource)

    def get_inventory_item(self, inventory_id):
        resource = '/inventory-items/%s' % inventory_id
        return self.get(resource)

    def update_inventory_item(self, inventory_id, data):
        resource = '/inventory-items/%s' % inventory_id
        return self.put(resource, data=data)

    def create_inventory_item(self, data):
        resource = '/inventory-items'
        return self.post(resource, data=data)

    def delete_inventory_item(self, inventory_id):
        resource = '/inventory-items/%s' % inventory_id
        return self.delete(resource)


class StoreSettingsClient(OrderDeskBaseClient):

    def get_store_settings(self):
        resource = '/store'
        return self.get(resource)


class OrderDeskClient(
        TestClient, OrderClient, OrderHistoryClient,
        MoveOrdersClient, OrderItemClient,
        ShipmentClient, InventoryClient,
        StoreSettingsClient):
    pass

from base import OrderDeskBaseClient


class TestClient(OrderDeskBaseClient):

    def test_connection(self):
        return self.get('test', {})


class OrderClient(OrderDeskBaseClient):
    def get_order(self, order_id):
        return self.get(
            'orders/%s' % order_id)

    def get_orders(self, data):
        return self.get(
            'orders', data=data)

    def create_order(self, data):
        return self.post(
            'orders', data=data)

    def update_order(self, order_id, data):
        return self.put(
            'orders/%s' % order_id, data=data)

    def delete_order(self, order_id):
        return self.delete(
            'orders/%s' % order_id)


class MoveOrdersClient(OrderDeskBaseClient):
    def move_orders(self, data):
        return self.post(
            'move-orders',
            data)


class OrderHistoryClient(OrderDeskBaseClient):

    def create_order_history_item(self, order_id, data):
        return self.post(
            'orders/%s/order-history' % order_id,
            data=data)


class OrderItemClient(OrderDeskBaseClient):

    def get_order_items(self, order_id):
        return self.get(
            'orders/%s/order-items' % order_id)

    def get_order_item(self, order_id, order_item_id):
        return self.get(
            'orders/%s/order-items/%s' % (
                order_id, order_item_id))

    def create_order_item(self, order_id, data):
        return self.post(
            'orders/%s/order-items/%s' % order_id,
            data=data)

    def update_order_item(self, order_id, order_item_id, data):
        return self.put(
            'orders/%s/order-items/%s' % (
                order_id, order_item_id),
            data=data)

    def delete_order_item(self, order_id, order_item_id):
        return self.delete(
            'orders/%s/order-items/%s' % (
                order_id, order_item_id))


class ShipmentClient(OrderDeskBaseClient):

    def get_order_shipments(self, order_id):
        return self.get(
            'orders/%s/shipments' % order_id)

    def get_order_shipment(self, order_id, shipment_id):
        return self.get(
            'orders/%s/shipments/%s' % (
                order_id, shipment_id))

    def create_shipment(self, order_id, data):
        return self.post(
            'orders/%s' % order_id,
            data=data)

    def delete_shipment(self, order_id, shipment_id):
        return self.delete(
            'orders/%s' % order_id)


class InventoryClient(OrderDeskBaseClient):

    def get_inventory_items(self):
        return self.get(
            'inventory-items')

    def get_inventory_item(self, inventory_id):
        return self.get(
            'inventory-items/%s' % inventory_id)

    def update_inventory_item(self, inventory_id, data):
        return self.put(
            'inventory-items/%s' % inventory_id,
            data=data)

    def create_inventory_item(self, data):
        return self.post(
            'inventory-items',
            data=data)

    def delete_inventory_item(self, inventory_id):
        return self.delete(
            'inventory-items/%s' % inventory_id)


class StoreSettingsClient(OrderDeskBaseClient):

    def get_store_settings(self):
        return self.get(
            'store')


class OrderDeskClient(
        TestClient, OrderClient, OrderHistoryClient,
        MoveOrdersClient, OrderItemClient,
        ShipmentClient, InventoryClient,
        StoreSettingsClient):
    pass

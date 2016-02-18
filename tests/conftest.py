from orderdesk import get_client

import pytest


@pytest.fixture
def client():
    client = get_client()
    return client


# From OrderDesk documentation - http://apidocs.orderdesk.me/#orders
@pytest.fixture
def order():
    order = {
        'email': 'test@orderdesk.me',
        'shipping_method': 'FedEx Home Delivery',
        'quantity_total': 1,
        'weight_total': 1,
        'product_total': 10,
        'shipping_total': 11.17,
        'handling_total': 0.5,
        'tax_total': 1.2,
        'discount_total': 1.7,
        'order_total': 21.17,
        'cc_number_masked': 'xxxxxxxxxxxx4242',
        'cc_exp': '02\/2016',
        'processor_response': 'Authorize.net Transaction ID: 2221864944',
        'payment_type': 'Visa',
        'payment_status': 'Approved',
        'processor_balance': 21.17,
        'customer_id': '5487542',
        'email_count': '3',
        'ip_address': '254.565.44.15',
        'tag_color': '',
        'source_name': 'Order Desk',
        'fulfillment_name': '',
        'fulfillment_id': '',
        'tag_name': 'success',
        'folder_id': 1,
        'date_added': '2014-10-08 12:10:00',
        'date_updated': '2014-10-09 23:13:47',
        'shipping': {
            'first_name': 'Jimmy',
            'last_name': 'Dean',
            'company': '',
            'address1': '800 Emmet St',
            'address2': '',
            'address3': '',
            'address4': '',
            'city': 'Nashville',
            'state': 'TN',
            'postal_code': '55555',
            'country': 'US',
            'phone': ''
        },
        'customer': {
            'first_name': 'Bingo',
            'last_name': 'Little',
            'company': '',
            'address1': '900 Lord Business Ave',
            'address2': '',
            'city': 'Knoxville',
            'state': 'TN',
            'postal_code': '77777',
            'country': 'US',
            'phone': ''
        },
        'return_address': {
            'title': 'Acme',
            'name': 'Doug Jones',
            'company': 'Acme Manufacturing',
            'address1': '817 E Maple Ln',
            'address2': '',
            'city': 'Knoxville',
            'state': 'TN',
            'postal_code': '55555',
            'country': 'US',
            'phone': ''
        },
        'checkout_data': {
            'Gift Message': 'Happy Birthday'
        },
        'order_metadata': {
            'fraud_protection_score': 0
        },
        'discount_list': [
            {
                'name': 'Discount',
                'code': 'MN234DX78',
                'amount': '1.70'
            }
        ],
        'order_notes': [
            {
                'date_added': '2014-10-09 23:12:05',
                'username': 'Customer Service Rep',
                'content': 'Customer called to change shipping address'
            }
        ],
        'order_items': [
            {
                'id': '42286',
                'name': 'Crazy Glue',
                'price': '10',
                'quantity': 1,
                'weight': 1,
                'code': 'crzyg-554',
                'delivery_type': 'ship',
                'category_code': 'DEFAULT',
                'variation_list': {
                    'Size': 'Small',
                    'Color': 'Black',
                },
                'metadata': {
                    'image': 'image_url_here'
                }
            }
        ],
        'order_shipments': [
            {
                'id': '369',
                'order_id': '26211',
                'store_id': '11',
                'tracking_number': '1Z132456789',
                'carrier_code': '',
                'shipment_method': '',
                'weight': '0',
                'cost': '0',
                'status': '',
                'tracking_url': '',
                'label_format': '',
                'label_image': '',
                'order_items': '',
                'print_status': '1',
                'cart_shipment_id': '',
                'date_shipped': '2014-10-09',
                'date_added': '2014-10-09 23:08:49'
            }
        ]
    }

    return order

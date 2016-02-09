

ORDER_PROPERTIES = [
    'id', 'source_id', 'source_name', 'source_id',
    'email', 'shipping_method', 'quantity_total',
    'weight_total', 'product_total', 'shipping_total',
    'handling_total', 'tax_total', 'discount_total',
    'order_total', 'cc_number', 'cc_exp', 'processor_response',
    'payment_type', 'payment_status', 'processor_balance',
    'customer_id', 'email_count', 'ip_address',
    'tag_color', 'tag_name', 'fulfillment_name',
    'fulfillment_id', 'folder_id', 'date_added',
    'date_updated', 'checkout_data', 'order_metadata',
    'shipping', 'customer', 'return_address', 'discount_list',
    'order_notes', 'order_shipments']


ORDER_ITEM_PROPERTIES = []

ADDRESS_PROPERTIES = [
    'first_name', 'last_name', 'company',
    'address1', 'address2', 'address3', 'address4',
    'city', 'state', 'postal_code', 'country', 'phone']


RETURN_ADDRESS_PROPERTIES = [
    'title', 'name', 'company', 'address1', 'address2',
    'city', 'state', 'postal_code', 'country', 'phone'
]

DISCOUNT_PROPERTIES = [
    'name', 'code', 'amount'
]

ORDER_NOTE_PROPERTIES = [
    'date_added', 'username', 'content'
]

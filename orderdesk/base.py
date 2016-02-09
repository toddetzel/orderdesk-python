from urlparse import urljoin

import os
import requests


class OrderDeskException(Exception):
    def __init__(self, status_code=None, reason=None):
        message = 'HTTP %s from OrderDesk: %s' % (
            status_code, reason)
        Exception.__init__(self, message)


class OrderDeskBaseClient(object):
    def __init__(self, store_id=None, apikey=None):
        self.endpoint = 'https://app.orderdesk.me/api/v2/'
        self.store_id = os.environ.get('ORDERDESK_STORE_ID', store_id)
        self.apikey = os.environ.get('ORDERDESK_APIKEY', apikey)

        if not self.store_id:
            raise ValueError(
                'Please specify ORDERDESK_STORE_ID in your environment '
                'or through the client as `store_id`')

        if not self.apikey:
            raise ValueError(
                'Please specify ORDERDESK_APIKEY in your environment '
                'or through the client as `apikey`')

        self.headers = {
            'ORDERDESK-STORE-ID': self.store_id,
            'ORDERDESK-API-KEY': self.apikey,
            'Content-Type': 'application/json',
        }

    def get(self, method, data={}):
        return requests.get(
            urljoin(self.endpoint, method),
            params=dict(data),
            headers=self.headers)

    def post(self, method, data={}):
        return requests.post(
            urljoin(self.endpoint, method),
            data=dict(data),
            headers=self.headers)

    def put(self, method, data={}):
        return requests.put(
            urljoin(self.endpoint, method),
            data=dict(data),
            headers=self.headers)

    def delete(self, method={}):
        return requests.delete(
            urljoin(self.endpoint, method),
            headers=self.headers)

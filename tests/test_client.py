import pytest


def test_connection(client):
    data = client.test_connection()

    assert data.get('status') == 'success'
    assert data.get('execution_time')
    assert data.get('message') == 'Connection Successful'
    assert data.get('current_date_time')

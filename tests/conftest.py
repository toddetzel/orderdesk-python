from orderdesk import get_client

import pytest


@pytest.fixture
def client(autouse=True):
    client = get_client()
    return client

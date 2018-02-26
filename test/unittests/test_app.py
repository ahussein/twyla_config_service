"""
Unittests for the application endpoints
"""

import init
from app.app import app


def test_healthcheck():
    """
    Unit test for healthcheck endpoint
    """
    _, response = app.test_client.get('/v1/')
    assert response.status == 200



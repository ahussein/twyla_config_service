"""
Unittests for the application endpoints
"""
import os
import sys
base_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(base_path)

app_path = os.path.join(base_path, 'app')
sys.path.append(app_path)

import pytest
import json

# fixture to load some test data
base_data_template = {
    "tenant": "acme{}",
    "integration_type": "flight-information-system{}",
    "configuration": {
        "username": "acme_user",
        "password": "acme12345",
        "wsdl_urls": {
        "session_url": "https://session.manager.svc",
        "booking_url": "https://booking.manager.svc"}
    }
}

@pytest.fixture
def load_base_data():
    from app.app import app 
    for index in range(10):
        item =  base_data_template.copy()
        item['tenant'] = item['tenant'].format(index)
        item['integration_type'] = item['integration_type'].format(index)

        app.test_client.post('/v1/config', data=json.dumps(item))
    

def test_healthcheck():
    """
    Test for / endpoint
    """
    from app.app import app    
    _, response = app.test_client.get('/v1/')
    assert response.status == 200


def test_get_config_not_valid():
    """
    Test for /config GET endpoint
    """
    import app
    _, response = app.app.app.test_client.get('/v1/config/')
    assert response.status == 400

def test_get_config_no_match_found():
    """
    Test for /config GET endpoint
    """
    import app
    _, response = app.app.app.test_client.get('/v1/config?tenant=non&integration_type=flight-information-system')
    assert response.status == 404
    assert response.json == {'result': "No matching data found"}


@pytest.mark.usefixtures("load_base_data")
def test_get_config_ok():
    """
    Test for /config GET endpoint
    """
    from app.app import app
    _, response = app.test_client.get('/v1/config?tenant=acme0&integration_type=flight-information-system0')
    assert response.status == 200
    assert response.json['result'] == {
    "tenant": "acme0",
    "integration_type": "flight-information-system0",
    "configuration": {
        "username": "acme_user",
        "password": "acme12345",
        "wsdl_urls": {
        "session_url": "https://session.manager.svc",
        "booking_url": "https://booking.manager.svc"}
    }
}


@pytest.mark.usefixtures("load_base_data")
def test_post_config_wrong_input_data():
    """
    Test for /config POST endpoint
    """
    from app.app import app
    _, response = app.test_client.post('/v1/config')
    assert response.status == 400
    assert response.json == {"status": "Wrong input data"}


@pytest.mark.usefixtures("load_base_data")
def test_post_config_missing_key():
    """
    Test for /config POST endpoint
    """
    from app.app import app
    _, response = app.test_client.post('/v1/config', data=json.dumps({
        "tenant": "acme0",
    "integration_type": "flight-information-system0",
    "configuration0": {
        "username": "acme_user",
        "password": "acme12345",
        "wsdl_urls": {
        "session_url": "https://session.manager.svc",
        "booking_url": "https://booking.manager.svc"}
    }
    }))
    assert response.status == 400
    

def test_post_config_new_item():
    """
    Test for /config POST endpoint
    """
    from app.app import app
    _, response = app.test_client.post('/v1/config', data=json.dumps({
        "tenant": "testitem",
    "integration_type": "testtype",
    "configuration": {
        "username": "acme_user",
        "password": "acme12345",
        "wsdl_urls": {
        "session_url": "https://session.manager.svc",
        "booking_url": "https://booking.manager.svc"}
    }
    }))
    assert response.status == 202


@pytest.mark.usefixtures("load_base_data")
def test_post_config_existing_item():
    """
    Test for /config POST endpoint
    """
    from app.app import app
    _, response = app.test_client.post('/v1/config', data=json.dumps({
        "tenant": "acme0",
    "integration_type": "flight-information-system0",
    "configuration": {
        "username": "new_user",
        "password": "acme12345",
        "wsdl_urls": {
        "session_url": "https://session.manager.svc",
        "booking_url": "https://booking.manager.svc"}
    }
    }))
    assert response.status == 202

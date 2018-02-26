"""
Test utils module
"""
import init
from app.utils import validate_inputs_for_post, validate_inputs_for_get

def test_validate_inputs_for_post_ok():
    """
    Test validate inputs for post data
    """
    input_data = {"tenant": "acme",
                "integration_type": "flight-information-system",
                "configuration": {
                "username": "acme_user",
                "password": "acme12345",
                "wsdl_urls": {
                "session_url": "https://session.manager.svc",
                "booking_url": "https://booking.manager.svc"}}}
    assert validate_inputs_for_post(data=input_data) == True

def test_validate_inputs_for_post_not_ok():
    input_data = {
            "tenant": "acme",
            "configuration": {
            "username": "acme_user",
            "password": "acme12345",
            "wsdl_urls": {
            "session_url": "https://session.manager.svc",
            "booking_url": "https://booking.manager.svc"
            }
        }
    }

    assert validate_inputs_for_post(data=input_data) == False

def test_validate_inputs_for_post_not_ok2():
    input_data = {"tenant": "acme",
                    "integration_type": "flight-information-system",
                    "configuration": {}
                    }
    assert validate_inputs_for_post(data=input_data) == False


def test_validate_inputs_for_get_ok():
    input_data = {"tenant": "acme",
"integration_type": "flight-information-system",
}
    assert validate_inputs_for_get(data=input_data) == True


def test_validate_inputs_for_get_not_ok():
    input_data = {"tenant": "acme",
"integration_type2": "flight-information-system",
}
    assert validate_inputs_for_get(data=input_data) == False
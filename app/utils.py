"""
Utils module for common functionalities
"""
import logging

REQUIRED_KEYS_GET = ('tenant', 'integration_type')
REQUIRED_KEYS_POST = REQUIRED_KEYS_GET + ('configuration',)

MISSING_KEY_POST_MSG = 'Not all required keys are provided in input data. Please make sure the following keys \
{} are included and configuration key is not empty'.format(REQUIRED_KEYS_POST)

MISSING_KEY_GET_MSG = "Not all required keys are proviced in filter data. Please make sure the following keys \
{} are included in the query string.".format(REQUIRED_KEYS_GET) 


def validate_inputs(data, request_type='get'):
    """
    Validates input data
    """
    valid = True
    required_keys = REQUIRED_KEYS_GET if request_type == 'get' else REQUIRED_KEYS_POST
    for key in required_keys:
        if key not in data:
            valid = False
            break
    if request_type == 'post':
        if type(data['configuration']) is not dict or not data['configuration']:
            valid = False
    return valid

def validate_inputs_for_post(data):
    """
    Validates that input data are valid for adding new configuration
    """
    return validate_inputs(data=data, request_type='post')

def validate_inputs_for_get(data):
    """
    Validates that query filters are valid
    """
    return validate_inputs(data=data, request_type='get')
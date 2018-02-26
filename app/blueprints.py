"""
Definining blueprints for routing
"""
from sanic.response import json
from sanic import Blueprint
from sanic_openapi import doc
import logging
import traceback
import config_manager
import utils


# define blueprint for api version 1
bp_api_v1 = Blueprint('v1', url_prefix='/v1')

@bp_api_v1.route('/', methods=['GET'])
@doc.summary("A health check endpoint")
async def healthcheck(request):
    """
    A health check endpoint
    """
    logging.info('hello!')
    return json({"status": "OK"}, 200)


@bp_api_v1.route('/config', methods=['POST'])
@doc.summary("Add new configuration item")
@doc.consumes({"tenant": str,
                "integration_type": str,
                "configuration": object}, location="body")
async def add_config(request):
    """
    An endpoint to add new configuration item
    """
    body = request.json
    if body:
        try:
            valid = utils.validate_inputs_for_post(data=body)
            if valid:
                await config_manager.add(data=body)
            else:
                return json({"status": utils.MISSING_KEY_POST_MSG}, 400)        
            return json({"status": "Created"}, 202)
        except Exception as ex:
            logging.error('Error while parsing request body: {}'.format(traceback.format_exc()))
            return json({"status": "Error while parsing request body"}, 400)
        
    else:
        logging.error('Request body {} does not have the correct input data'.format(body))
        return json({"status": "Wrong input data"}, 400)


@bp_api_v1.route('/config', methods=['GET'])
@doc.summary('Retrieves an existing configurations based on filtering parameters')
@doc.produces({"result": 
    {"tenant": str,
                "integration_type": str,
                "configuration": object}
})
async def get_config(request):
    """
    An endpoint to retrieves an existing configurations based on filtering parameteprs
    """
    args = request.raw_args
    if args:
        valid = utils.validate_inputs_for_get(data=args)
        if valid:
            _, item = await config_manager.get(data=args)
            if item:
                return json({'result': item}, 200)
            else:
                return json({'result': 'No matching data found'}, 404)

        else:
            return json({"status": utils.MISSING_KEY_GET_MSG}, 400) 
    else:
        logging.error('Request arguments {} does not have the correct filters'.format(args))
        return json({"status": "Wrong qeury filters"}, 400)
    


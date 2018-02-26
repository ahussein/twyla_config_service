"""
Module contains bussiness logic for managing configurations
"""

import logging
from models import Configuration



async def get(data):
    """
    Retrieves a configuration item from the database
    """
    item = await Configuration.find_one({'tenant': data['tenant'], 
                                         'integration_type': data['integration_type']})
    item_id = item.id
    item.__dict__.pop('_id')
    return item_id, item.__dict__


async def add(data):
    """
    Adds a new configuration item to the database or update an existing one
    """
    item_id, item = await get(data=data)
    if item:
        logging.info('Item with tenant: {} and integration_type {} already exist. Updating it'.format(
            data['tenant'], data['integration_type']
        ))
        item['configuration'].update(data['configuration'])
        return await Configuration.update_one({'_id': item_id}, {'$set': item})
    else:
        return await Configuration.insert_one(data)


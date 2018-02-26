"""
Data access module
"""

from sanic_motor import BaseModel

def initialize_model(db_uri, app):
    """
    Initializes the connectoin to the backend database

    @param db_uri: connection string to the mongodb instance
    @param app: Sanic application object
    """
    settings = {
        'MOTOR_URI': db_uri
    }
    app.config.update(settings)
    BaseModel.init_app(app)


class Configuration(BaseModel):
    """
    Configuration class representing a configuration item
    """
    __coll__ = 'configs'
    __unique_fields__ = ['tenant']

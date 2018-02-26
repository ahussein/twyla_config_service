"""
Application entry point
"""

from sanic import Sanic
from blueprints import bp_api_v1
from models import Configuration, initialize_model
import logging
from sanic_openapi import swagger_blueprint, openapi_blueprint
import os

# This should be configured in a configuration file or evnironment varaiable
DEFAULT_DB_URI = 'mongodb://localhost:27017/twyla_configs'


# configure logger, this should be done much better than this.
logging.basicConfig(filename='server.log',level=logging.DEBUG,
                    format='%(asctime)s - (%(name)s)[%(levelname)s: %(message)s')

# create application object
app = Sanic(__name__)

# register blueprints
app.blueprint(bp_api_v1)
app.blueprint(swagger_blueprint)
app.blueprint(openapi_blueprint)

# setup swager configurations, better load this from a config file or use api-dirven approache
app.config.API_VERSION = '0.1.0'
app.config.API_TITLE = 'Twyla Configuration Service'
app.config.API_DESCRIPTION = 'Configuration management service for Twyla'
app.config.API_TERMS_OF_SERVICE = 'Use for demo!'
app.config.API_PRODUCES_CONTENT_TYPES = ['application/json']
app.config.API_CONTACT_EMAIL = 'ahussein.abdelrahman@gmail.com'

# configure models
initialize_model(db_uri=os.environ.get('DB_URI', DEFAULT_DB_URI), app=app)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=False)
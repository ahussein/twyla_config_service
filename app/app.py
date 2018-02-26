"""
Application entry point
"""

from sanic import Sanic
from blueprints import bp_api_v1
from models import Configuration, initialize_model
import logging

# This should be configured in a configuration file or evnironment varaiable
DB_URI = 'mongodb://localhost:27017/twyla_configs'


# configure logger, this should be done much better than this.
logging.basicConfig(filename='server.log',level=logging.DEBUG,
                    format='%(asctime)s - (%(name)s)[%(levelname)s: %(message)s')

# create application object
app = Sanic(__name__)

# register blueprints
app.blueprint(bp_api_v1)

# configure models
initialize_model(db_uri=DB_URI, app=app)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
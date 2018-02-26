# Twyla Configuration service

.. image:: https://travis-ci.org/ahussein/twyla_config_service.svg?branch=master
    :target: https://travis-ci.org/ahussein/twyla_config_service

.. image:: https://codecov.io/gh/ahussein/twyla_config_service/branch/master/graphs/badge.svg
  :target: https://codecov.io/gh/ahussein/twyla_config_service


------------------------
Development Installation
------------------------

To install for development, activate your virtualenv and
do::

    git clone https://github.com/ahussein/twyla_config_service.git
    cd twyla_config_service
    pip install -r requirements.txt
    pip install -e .

**Make sure your virtualenv is activated for the rest of the commands in this page.**

To run the app, you need a DB instance running and you can use an environment variable to point to your running
DB instance like the following::

    export DB_URI='mongodb://localhost:27017/testdb'

If the environment is not set, then the app will try to connect to the following URI::

    mongodb://localhost:27017/twyla_configs
  
After making sure the DB instance is up and running you can start the app service using the following command::

    python3 app/app.py

-----------------
Running the Tests
-----------------

To run the tests with coverage report, do::

    pytest -v --cov=./app test

The above tests requires a DB instance to be running since it includes integration tests. To run only unittests do::

    pytest -v test/unittests
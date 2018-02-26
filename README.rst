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


-----------------
Load Testing The Service
-----------------
For load testing, I have picked up Locust_.
.. _Locust: https://locust.io/
It is python based, so tests are written in python and it has a nice UI as well. Make sure to have your virtualenv is activated and then::

        pip install locustio

I have prepared a simple load test script and you can run it with the following command (assuming that the service is running on localhost:8000)::
        locust -f load_test.py --no-web -c 1000 -r 10 --host=http://localhost:8000 --csv=load_test_result.csv

This will start the load tester with a 1000 user each of them is trying to execute a mixure of the the exposed endpoints. The above
command will run the load tests in no-ui mode and you can choose to run with the UI mode. Please check the docs for more details here: https://docs.locust.io/en/latest/what-is-locust.html
"""
This is a simple load test using locust library
"""


from locust import HttpLocust, TaskSet
import json

test_config = {
    "tenant": "acme",
    "integration_type": "flight-information-system",
    "configuration": {
        "username": "acme_user",
        "password": "acme12345",
        "wsdl_urls": {
        "session_url": "https://session.manager.svc",
        "booking_url": "https://booking.manager.svc"}
    }
}

def healthcheck(l):
    l.client.get("/v1/")

def get_config_not_ok(l):
    l.client.get("/v1/config")

def get_config_no_data_found(l):
    l.client.get("/v1/config?tenant=non&integration_type=flight-information-system")

def get_config_ok(l):
    l.client.get("/v1/config?tenant=acme&integration_type=flight-information-system")

def add_config(l):
    l.client.post("/v1/config/", json=test_config)

class UserBehavior(TaskSet):
    tasks = {
                healthcheck: 1, get_config_not_ok: 1, get_config_no_data_found: 1,
                get_config_ok: 3, add_config: 3,
            }

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
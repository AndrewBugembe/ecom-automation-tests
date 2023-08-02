
from shoppingtests.src.utilities.genericUtilities import get_random_email_password
from shoppingtests.src.utilities.requestapi import RequestApi
class CustomerHelper(object):

    def __init__(self):
        self.requests_utility = RequestApi()

    def create_customer(self, email=None, password=None, **kwargs):
        if not email:
            ep = get_random_email_password()
            email = ep['email']
        if not password:
            password = 'test123'
        payload = dict()
        payload['email'] = email
        payload['password'] = password
        payload.update(**kwargs)
        create_user_json = self.requests_utility.post("/customers", payload=payload, expected_status_code=201)
        return create_user_json


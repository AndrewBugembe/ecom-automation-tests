import requests
import os
import json
from requests_oauthlib import OAuth1
import logging as logger

from shoppingtests.src.configs.hosts_config import API_HOSTS
from shoppingtests.src.utilities.credentialUtilities import CredentialUtilities

class RequestApi(object):
    def __init__(self):

        # self.env = os.environ.get("ENV", "test")
        wc_credentials = CredentialUtilities.get_api_keys()
        self.auth = OAuth1(wc_credentials["wc_key"], wc_credentials["wc_secret"])
        self.base_url = API_HOSTS['test']

    def assert_status_code(self):
       assert self.status_code == self.expected_status_code, f'Bad response code '

    def post(self, endpoint="/customers", headers=None, payload=None, expected_status_code=201):
        if not headers:
            headers = {"Content-Type": "application/json"}
        url = self.base_url + endpoint

        rs_api = requests.post(url=url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        # assert self.status_code == int(expected_status_code),\
        # f'Expected status code is {expected_status_code} but it is {self.status_code}'
        return rs_api.json()
        logger.debug(f'API response: {rs_api.json()}')


        breakpoint()


    def get(self, endpoint, data):
        pass
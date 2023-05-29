import requests
import os
import json
from requests_oauthlib import OAuth1

from shoppingtests.src.configs.hosts_config import API_HOSTS
from shoppingtests.src.utilities.credentialUtilities import CredentialUtilities

class RequestApi(object):
    def __init__(self):

        # self.env = os.environ.get("ENV", "test")
        wc_credentials = CredentialUtilities.get_api_keys()
        self.auth = OAuth1(wc_credentials["wc_key"], wc_credentials["wc_secret"])
        self.base_url = API_HOSTS['test']

    def post(self, endpoint="/customers", headers=None, payload=None):
        if not headers:
            headers = {"Content-Type": "application/json"}
        url = self.base_url + endpoint

        rs_api = requests.post(url=url, data=json.dumps(payload), headers=headers, auth=self.auth)

        breakpoint()


    def get(self, endpoint, data):
        pass
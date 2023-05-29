import os


class CredentialUtilities(object):

    def __init__(self):
        pass
    @staticmethod
    def get_api_keys():
        wc_key = os.environ.get('WC_KEY')
        wc_secret = os.environ.get('WC_SECRET')

        if not wc_key or not wc_secret:
            raise Exception("API 'WC_KEY' and 'WC_SECRET' must be variables in the env")
        else:
            return {"wc_key": wc_key, "wc_secret": wc_secret}
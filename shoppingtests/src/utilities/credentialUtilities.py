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
            return {"WC_KEY": wc_key, "WC_SECRET": wc_secret}

    @staticmethod
    def get_db_creds():
        db_user = os.environ.get('DB_USER')
        db_password = os.environ.get('DB_PASSWORD')

        if not db_user or not db_password:
            raise Exception("Database credentials 'DB_USER' and 'DB_PASSWORD' must be variables in the env")
        else:
            return {"db_user": db_user, "db_password": db_password}
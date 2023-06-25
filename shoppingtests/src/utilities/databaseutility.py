import  pymysql
from shoppingtests.src.utilities.credentialUtilities import CredentialUtilities
class ConnectToDb(object):
    def __init__(self):
        sign_cred = CredentialUtilities
        self.creds = sign_cred.get_db_creds()
        # self.host = "localhost"


    def create_connection(self):
        # self.creds = sql_creds
        connection = pymysql.connect(host="localhost", user=self.creds["db_user"], password=self.creds["db_password"], port=8889)
        return connection

    def execute_select(self, sql):
        conn = self.create_connection()
        try:
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            rs_dict = cur.fetchall()
            cur.close()
        except Exception as e:
            raise Exception(f"Failed to connect to {sql}")
        finally:
            conn.close()
        return rs_dict

    def execute_sql(self,sql):
        pass



from shoppingtests.src.utilities.databaseutility import ConnectToDb
import random

class CustomerFromDb(object):
    def __init__(self):
        self.cus_db = ConnectToDb()

    def get_customer_by_email(self, email):
        sql = f"select * from shopping.wp_users where user_email = '{email}';"
        cus_from_sql = self.cus_db.execute_select(sql)
        return cus_from_sql

    def get_random_customer_from_db(self, qty=1):
        sql = "select * from shopping.wp_users order by ID desc limit 5000;"
        cus_from_db = self.cus_db.execute_select(sql)
        random_cus = random.sample(cus_from_db, int(qty))
        return random_cus

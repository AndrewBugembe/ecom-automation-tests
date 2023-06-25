from shoppingtests.src.utilities.databaseutility import ConnectToDb

class CustomerFromDb(object):
    def __init__(self):
        self.cus_db = ConnectToDb()

    def get_customer_by_email(self, email):
        sql = f"select * from shopping.wp_users where user_email = '{email}';"
        cus_from_sql = self.cus_db.execute_select(sql)
        breakpoint()
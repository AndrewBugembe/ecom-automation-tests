from shoppingtests.src.utilities.databaseutility import ConnectToDb
import random


class ProductFromDb:
    def __init__(self):
        self.prod_db = ConnectToDb()

    def get_random_product(self, qty=1):
        sql = f"select ID, post_title from shopping.wp_posts where post_type = 'product' limit 100;"
        sql_helper = self.prod_db.execute_select(sql)
        return random.sample(sql_helper, int(qty))




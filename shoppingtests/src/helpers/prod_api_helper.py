from shoppingtests.src.utilities.requestapi import RequestApi

class ProductHelper:
    def __init__(self):
        self.request_utility = RequestApi()

    def get_product_id(self, product_id):
        return self.request_utility.get('products/product_id')

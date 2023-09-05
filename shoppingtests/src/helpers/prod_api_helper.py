from shoppingtests.src.utilities.wooAPIutility import WooAPIUtility

class ProductHelper:
    def __init__(self):
        self.api_utility = WooAPIUtility()

    def get_product_id(self, product_id):
        return self.api_utility.get('products/product_id')

    def get_product(self, products):
        return self.api_utility.get('products')

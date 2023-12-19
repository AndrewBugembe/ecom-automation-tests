import pytest
from shoppingtests.src.DAO.productDAO import ProductFromDb
from shoppingtests.src.helpers.prod_api_helper import ProductHelper

@pytest.mark.product
@pytest.mark.tb7
def test_update_random_product_regular_price():

    """get random product from db"""
    prod = ProductFromDb()
    rand_prod = prod.get_random_product(1)
    prod_id = rand_prod[0]["ID"]

    """update product price and make an api call to update the regular price"""
    api_call = ProductHelper()
    data = {'regular_price': '5'}
    api_update = api_call.update_product(prod_id, data)

    """verify product regular price has been updated to new price"""
    assert api_update['regular_price'] == data['regular_price'], "new regular price should be 5"

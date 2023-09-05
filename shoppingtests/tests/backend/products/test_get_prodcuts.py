import pytest

from shoppingtests.src.DAO.productDAO import ProductFromDb
from shoppingtests.src.helpers.prod_api_helper import ProductHelper
import logging as logger
 @pytest.mark.product
 @pytest.mark.tb1
 def test_get_products_by_id():

     #get random product from db, can also get a list from using api calls
     prod_db = ProductFromDb()
     prod = prod_db.get_random_product()
     prod_id = prod[0]['ID']
     prod_name = prod[0]['post_name']
     prod_title = prod[0]['post_title']

     # make api call
     api_prod = ProductHelper()
     rs_api = api_prod.get_product_id(prod_id)

     # verify response
     assert rs_api[0]['post_name'] == prod_name, f"Expected product name should match product name from the database"


@pytest.mark.product
@pytest.mark.tb
def test_get_products_not_empty():

 # make aoi call
    prod_api = ProductHelper()
    rs_api = prod_api.get_product('products')

 # verify response
    assert rs_api[0], f"Item should not be empty"




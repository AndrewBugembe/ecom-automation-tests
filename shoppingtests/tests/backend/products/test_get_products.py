import pytest
from shoppingtests.src.utilities.requestapi import RequestApi
<<<<<<< HEAD
from shoppingtests.src.DAO.productDAO import ProductFromDb
from shoppingtests.src.helpers.prod_api_helper import ProductHelper
import logging as logger



@pytest.mark.product
=======


@pytest.mark.customer
>>>>>>> d7cf80e60b0b5a5878cd899d5178c204239a11d8
@pytest.mark.tb4
def test_get_products():
    get_api = RequestApi()
    get_products = get_api.get("products")
<<<<<<< HEAD
    return get_products

@pytest.mark.product
@pytest.mark.tb5
def test_get_random_product_by_id():

#get product id from db
    get_prod = ProductFromDb()
    prod_db = get_prod.get_random_product(1)
    prod_db_id = prod_db[0]["ID"]
    logger.info(f"The ID is: {prod_db_id}")
#make api call
    rs_api = ProductHelper()
    rs_api_response = rs_api.get_product_id(prod_db_id)
    # assert rs_api_response["ID"] == prod_db_id, "The ID does not much"
    breakpoint()
# # extract JSON response
#     rs_api_prod = rs_api_response.json()
#     breakpoint()
#     # return rs_api_prod
#     #assert response
#     assert prod_db[0]['post_title'] == rs_api_prod[0]["name"], "Something did not work"

=======
    breakpoint()
    return get_products
>>>>>>> d7cf80e60b0b5a5878cd899d5178c204239a11d8

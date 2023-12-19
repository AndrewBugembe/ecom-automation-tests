import pytest

from shoppingtests.src.DAO.productDAO import ProductFromDb
from shoppingtests.src.helpers.prod_api_helper import ProductHelper


@pytest.mark.product
@pytest.mark.tb6
def test_delete_product():

    # get random product from db
    rand_prod = ProductFromDb()
    product = rand_prod.get_random_product()
    prod_id = product[0]['ID']

    # make api call with product to delete
    prod_api = ProductHelper()
    rs_api = prod_api.delete_product(prod_id)


    # verify product is deleted,  using an api call

    verify_prod_deleted = prod_api.delete_product(prod_id)
    expected_message = 'The product has already been deleted.'
    assert verify_prod_deleted['message'] == expected_message, f"The product does not seem to be deleted, " \
                                                               f"expected message should be {expected_message}"





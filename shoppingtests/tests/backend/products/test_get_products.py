import pytest
from shoppingtests.src.utilities.requestapi import RequestApi


@pytest.mark.customer
@pytest.mark.tb4
def test_get_products():
    get_api = RequestApi()
    get_products = get_api.get("products")
    breakpoint()
    return get_products
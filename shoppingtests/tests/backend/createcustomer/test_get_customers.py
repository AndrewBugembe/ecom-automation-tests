import pytest
from shoppingtests.src.utilities.requestapi import RequestApi

@pytest.mark.customer
@pytest.mark.tb3
def test_get_all_customers():
    get_api = RequestApi()
    get_customer = get_api.get("customers?order=desc&orderby=id")
    breakpoint()
    return get_customer

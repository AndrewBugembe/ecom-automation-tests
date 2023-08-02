import pytest
from shoppingtests.src.utilities.requestapi import RequestApi

@pytest.mark.customer
@pytest.mark.tb3
def test_get_all_customers():
    get_api = RequestApi()
    get_customer = get_api.get("customers?order=desc&orderby=id")
<<<<<<< HEAD
    breakpoint()
=======
>>>>>>> d7cf80e60b0b5a5878cd899d5178c204239a11d8
    return get_customer

import pytest
import logging as logger
from shoppingtests.src.utilities.genericUtilities import get_random_email_password
from shoppingtests.src.helpers.apihelpers import CustomerHelper

@pytest.mark.tb1
def test_create_customer_email():
    logger.debug("Create customer")
# generate random email and password
    rand_info = get_random_email_password()
    email = rand_info['email']
    password = rand_info['password']
    payload = {'email': email, 'password': password}
    # return payload
# make api call
    customer_object = CustomerHelper()
    customer_api = customer_object.create_customer(email=email, passwordc=password)
    breakpoint()

# assert status code
# assert email is created
# assert customer is creatred

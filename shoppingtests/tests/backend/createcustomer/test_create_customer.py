import pytest
import logging as logger
from shoppingtests.src.utilities.genericUtilities import get_random_email_password
from shoppingtests.src.helpers.apihelpers import CustomerHelper
from shoppingtests.src.DAO.customerDAO import CustomerFromDb

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
    customer_api = customer_object.create_customer(email=email, password=password)
    # assert customer and email are created

    assert customer_api["email"] == email, f'Email does not match. Email: {email}'
    assert customer_api["first_name"] == '', f'First name should be empty'

# verify customer created in database
    customer_in_db = CustomerFromDb()
    cuz = customer_in_db.get_customer_by_email(email)

    breakpoint()

# assert status code


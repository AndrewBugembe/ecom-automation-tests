import pytest
import logging as logger
from shoppingtests.src.utilities.genericUtilities import get_random_email_password
from shoppingtests.src.helpers.api_cus_helpers import CustomerHelper
from shoppingtests.src.DAO.customerDAO import CustomerFromDb
from shoppingtests.src.utilities.requestapi import RequestApi

@pytest.mark.customer
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
    breakpoint()

    # assert customer and email are created
    assert customer_api["email"] == email, f'Email does not match. Email: {email}'
    assert customer_api["first_name"] == '', f'First name should be empty'

    # verify customer created in database
    customer_db = CustomerFromDb()
    customer_info = customer_db.get_customer_by_email(email)
    print(customer_info)
    breakpoint()

    # customer_in_db.get_customer_by_email(email)
    id_in_api = customer_api["email"]
    id_in_db = customer_info[0]["user_email"]
    assert id_in_api == id_in_db, f"Something is wrong"

    breakpoint()

# assert status code

# create customer using existing email
@pytest.mark.customer
@pytest.mark.tb2
def test_create_customer_fail_with_existing_email():
    # get existing email from db
    existing_cus_from_db = CustomerFromDb()
    cus_db = existing_cus_from_db.get_random_customer_from_db()
    existing_cus_email = cus_db[0]["user_email"]
    print(existing_cus_email)
    # call the  api
    customer_object = RequestApi()
    payload = {"email": existing_cus_email, "password": "password22"}
    customer_api = customer_object.post(endpoint="/customers", payload=payload, expected_status_code=400)
    # validate customer exists
    assert customer_api["code"] == "registration-error-email-exists", "Make sure email used is from existing users"
    breakpoint()



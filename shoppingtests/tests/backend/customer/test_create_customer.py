import pytest
import logging as logger
from shoppingtests.src.utilities.genericUtilities import get_random_email_password
from shoppingtests.src.DAO.customerDAO import CustomerFromDb
from shoppingtests.src.utilities.wooAPIutility import WooAPIUtility


@pytest.mark.customer
@pytest.mark.tb1
def test_create_customer_email():
    logger.debug("Create customer")
# generate random email and password
    rand_info = get_random_email_password()
    email = rand_info['email']
    password = rand_info['password']
    payload = {'email': email, 'password': password}

# make api call

    woo_helper = WooAPIUtility()
    rs_api = woo_helper.post("customers", params=payload, expected_status_code=201)

# assert customer and email are created
    assert rs_api["email"] == email, f'Email does not match. Email: {email}'
    assert rs_api["first_name"] == '', f'First name should be empty'

# verify customer created in database
    customer_db = CustomerFromDb()
    customer_info = customer_db.get_customer_by_email(email)
    assert customer_info['email'] == email, f"Created email should be the same as email in database"
    assert customer_info['id'], f"ID should be present"


@pytest.mark.customer
@pytest.mark.tb2
def test_create_customer_fail_with_existing_email():
    # get existing email from db
    existing_cus_from_db = CustomerFromDb()
    random_cus_db = existing_cus_from_db.get_random_customer_from_db()
    random_email = random_cus_db[0]["user_email"]
    print(random_email)
    logger.debug(f"email available is {random_email}")

    # call the  api
    password = get_random_email_password()
    random_password = password['password']
    payload = {'email': random_email, 'password': random_password}
    customer_from_api = WooAPIUtility()
    rs_api = customer_from_api.post('customers', params=payload, expected_status_code=400)

    # validate customer exists
    assert rs_api['code'] == 'registration-error-email-exists', f"Expected error should be:"\
                                                                f"registration-error-email-exists"
    assert rs_api['data']['status'] == 400, f"Expected status code should be 400"

    breakpoint()

@pytest.mark.customer
@pytest.mark.tb3
def test_customer_fail_with_email_no_password():
    # get random existing email from db
    existing_cus_from_db = CustomerFromDb()
    random_cus_db = existing_cus_from_db.get_random_customer_from_db()
    random_email = random_cus_db[0]["user_email"]
    print(random_email)
    logger.debug(f"email available is {random_email}")

    # call the  api
    payload = {'email': random_email}
    customer_from_api = WooAPIUtility()
    rs_api = customer_from_api.post('customers', params=payload, expected_status_code=400)

    # verify message output with no password
    assert rs_api['message'] == 'Missing parameter(s): password', f"The message without password should read:"\
                                                                    f"'Missing parameter(s): password'"


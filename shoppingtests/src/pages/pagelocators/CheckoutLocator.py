from selenium.webdriver.common.by import By

class CheckoutLocator:
    INPUT_BILLING_FIRSTNAME = (By.ID, "billing_first_name")
    INPUT_BILLING_LASTNAME = (By.ID, "billing_last_name")
    INPUT_BILLING_ADDRESS1 = (By.ID, "billing_address_1")
    INPUT_BILLING_CITY = (By.ID, "billing_city")
    INPUT_BILLING_ZIPCODE = (By.ID, "billing_postcode")
    INPUT_BILLING_EMAIL = (By.ID, "billing_email")
    INPUT_BILLING_PHONE = (By.ID, "billing_phone")
    SELECT_COUNTRY_DROPDOWN = (By.ID, "billing_country")
    SELECT_STATE_DROPDOWN = (By.ID, "billing_state")
    PLACE_ORDER_BTN = (By.ID, "place_order")

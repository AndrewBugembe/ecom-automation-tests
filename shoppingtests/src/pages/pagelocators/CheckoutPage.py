from shoppingtests.src.pages.pagelocators.seleniumlocator import SeleniumHelpers
from shoppingtests.src.pages.pagelocators.CheckoutLocator import CheckoutLocator
from shoppingtests.src.utilities.genericUtilities import get_random_email_password
from shoppingtests.src.configs.hosts_config import MainConfigs
class CheckoutPage(CheckoutLocator):
    endpoint = '/checkout'
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumHelpers(driver)

    def go_to_checkout_page(self):
        checkout = MainConfigs.get_base_url()
        url = checkout + self.endpoint
        self.driver.get(url)

    def input_billing_firstname(self, firstname=None):
        firstname = 'Automation_First' if not firstname else firstname
        self.sl.wait_and_input_text(self.INPUT_BILLING_FIRSTNAME, firstname)

    def input_billing_lastname(self, lastname=None):
        lastname= 'Automation_Last' if not lastname else lastname
        self.sl.wait_and_input_text(self.INPUT_BILLING_LASTNAME, lastname)

    def input_billing_address_1(self, address1=None):
        address1 = "235 Bolton st" if not address1 else address1
        self.sl.wait_and_input_text(self.INPUT_BILLING_ADDRESS1, address1)

    def input_billing_city(self, city=None):
        city= 'Boston' if not city else city
        self.sl.wait_and_input_text(self.INPUT_BILLING_CITY, city)

    def input_billing_zipcode(self, zipcode=None):
        zipcode = '02125' if not zipcode else zipcode
        self.sl.wait_and_input_text(self.INPUT_BILLING_ZIPCODE, zipcode)

    def input_billing_phone(self, phone=None):
        phone= '0222222' if not phone else phone
        self.sl.wait_and_input_text(self.INPUT_BILLING_PHONE, phone)

    def input_billing_email(self, email=None):
        if not email:
            rand_email = get_random_email_password()
            email = rand_email["email"]
            return email
        self.sl.wait_and_input_text(self.INPUT_BILLING_EMAIL, email)

    def fill_in_billing_info(self, f_name=None, l_name=None, address1=None, city=None, zipcode=None, phone=None,
                             email=None, state=None, country=None):
        self.input_billing_firstname(firstname=f_name)
        self.input_billing_lastname(lastname=l_name)
        self.input_billing_address_1(address1=address1)
        self.input_billing_city(city=city)
        self.input_billing_zipcode(zipcode=zipcode)
        self.input_billing_phone(phone=phone)
        self.input_billing_email(email=email)
        self.select_state_dropdown(state=state)
        self.select_country_dropdown(country=country)

    def select_country_dropdown(self, country=None):
        country = 'United States (US)' if not country else country
        self.sl.wait_and_select_dropdown(self.SELECT_COUNTRY_DROPDOWN, to_select=country, select_by="visible_text")

    def select_state_dropdown(self, state=None):
        state = 'Massachusetts' if not state else state
        self.sl.wait_and_select_dropdown(self.SELECT_STATE_DROPDOWN, to_select=state, select_by="visible_text")

    def place_order_btn(self):
        self.sl.wait_and_click(self.PLACE_ORDER_BTN)
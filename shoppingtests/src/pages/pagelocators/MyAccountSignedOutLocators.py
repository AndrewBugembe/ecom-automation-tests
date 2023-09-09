from selenium.webdriver.common.by import By

class MyAccountSignedOutLocator:

# login helpers
    LOGIN_USERNAME = (By.ID, "username")
    LOGIN_PASSWORD = (By.ID, "password")
    CLICK_LOGIN = (By.CSS_SELECTOR, "#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > button")
    ERROR_DISPLAYED = (By.CSS_SELECTOR, "#content > div > div.woocommerce > ul > li")
# register helpers
    REGISTER_EMAIL = (By.ID, "reg_email")
    REGISTER_PASSWORD = (By.ID, "reg_password")
    CLICK_REGISTER = (By.CSS_SELECTOR, "woocommerce-Button woocommerce-button button wp-element-button woocommerce-form-register__submit disabled")

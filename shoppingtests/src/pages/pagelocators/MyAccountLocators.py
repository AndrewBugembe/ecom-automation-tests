from selenium.webdriver.common.by import By

class MyAccountSignedOutLocator:
    LOGIN_USERNAME = (By.ID, "username")
    LOGIN_PASSWORD = (By.ID, "password")
    CLICK_LOGIN = (By.CSS_SELECTOR, "#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > button")
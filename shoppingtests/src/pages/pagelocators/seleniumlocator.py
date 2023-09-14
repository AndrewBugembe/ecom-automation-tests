from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class SeleniumHelpers:
    def __init__(self, driver):
        self.driver = driver
        self.def_timeout =20

    def wait_and_input_text(self,locator, text, timeout=None):
        timeout = timeout if timeout else self.def_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)).send_keys(text)

    def wait_and_click(self, locator, timeout=None):
        timeout = timeout if timeout else self.def_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)).click()

    def wait_until_error_is_displayed(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.def_timeout
        WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text)
        )

    def wait_until_element_is_visible(self, locator_or_element, timeout=None):
        timeout = timeout if timeout else timeout is self.def_timeout

        if isinstance(locator_or_element, tuple):
            elem = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator_or_element),
            message=f'Element {locator_or_element} not found after timeout of {timeout}')
        else:
            import selenium.webdriver.remote.webelement
            if isinstance(locator_or_element, selenium.webdriver.remote.webelement.WebElement):
                elem = WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of(locator_or_element),
                    message=f'Element {locator_or_element} not found after timeout of {timeout}')
            else:
                raise TypeError(f"Element must be a 'tuple' or 'WebElement' not {locator_or_element}")

        return elem




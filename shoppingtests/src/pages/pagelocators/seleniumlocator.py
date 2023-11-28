from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select


class SeleniumHelpers:
    def __init__(self, driver):
        self.driver = driver
        self.def_timeout = 20

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
        WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))

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

    def wait_until_element_contains_text(self, locator,text, timeout=None):
        timeout = timeout if timeout else timeout is self.def_timeout
        WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text),
                        message=f'Element {locator} does not contain {text} after timeout of {timeout}')

    def wait_and_get_elements(self, locator, timeout=None, error=None):
        timeout = timeout if timeout else self.def_timeout
        error = error if error else f" Unexpected {locator} and {timeout}  "
        # WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator),
        #                       message=f'Element {locator} not visible after timeout of {timeout}')
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator),
            )
        except TimeoutException:
            raise TimeoutException(error)

        return elements

    def wait_and_select_dropdown(self, locator, to_select, select_by='visible_text'):
        select_element = self.wait_until_element_is_visible(locator)
        select = Select(select_element)
        if select_by.lower() == 'visible_text':
            select.select_by_visible_text(to_select)
        elif select_by.lower() == 'index':
            select.select_by_index(to_select)
        elif select_by.lower() == 'value':
            select.select_by_value(to_select)
        else:
            raise Exception(
                f"Invalid option for 'to_select' parameter. Valid values are 'visible_text', 'index', or value 'value'.")

    def wait_and_get_text(self, locator, timeout=None):
        timeout = timeout if timeout else self.def_timeout
        elm = self.wait_until_element_is_visible(locator, timeout)
        element_text = elm.text
        return element_text

    # def wait_and_get_text(self, locator, text, timeout=None):
    #     timeout = timeout if timeout else self.def_timeout
    #     elm = WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))
    #     return elm





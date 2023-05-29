import pytest
from selenium import webdriver
import os

@pytest.fixture(scope="class")
def init_driver(request):

    available_browsers = ["chrome", "edge", "firefox"]
    browser = os.environ.get('BROWSER', None)
    if not browser:
        raise Exception("the environment variable you chose is not valid")
    browser = browser.lower()
    if browser not in available_browsers:
        raise Exception(f"you must choose from {available_browsers}")
    # elif browser == "chrome":
    #     driver = webdriver.Chrome()
    # elif browser == "edge":
    #     driver = webdriver.Edge()
    # else:
    #     driver = webdriver.Firefox()

    if browser in ('chrome'):
        driver = webdriver.Chrome()
    elif browser in ('edge'):
        driver = webdriver.Edge()

    request.cls.driver = driver
    yield
    driver.quit()
import pytest
from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options as ChrOptions
from selenium.webdriver.firefox.options import Options as FFOptions

@pytest.fixture(scope="class")
def init_driver(request):

    available_browsers = ["chrome", "edge", "firefox", "headlesschrome", "headlessfirefox"]
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
    elif browser in ("headlesschrome"):
        chrome_options = ChrOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(options=chrome_options)
    # elif browser in ("headlessfirefox"):
    #     firefox_options = FFOptions()
    #     firefox_options.add_argument()

    request.cls.driver = driver
    yield
    driver.quit()
import time

import pytest
from selenium import webdriver

@pytest.fixture(scope='class')
def setup():
    driver = webdriver.Edge()
    driver.get("https://demowebshop.tricentis.com/")
    time.sleep(2)
    yield driver
    driver.quit()

class TestRegister:
    def test_register(self,setup):
        driver = setup


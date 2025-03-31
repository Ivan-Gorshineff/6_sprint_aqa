import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


@pytest.fixture
def driver():
    service = Service()
    firefox_driver = webdriver.Firefox(service=service)
    firefox_driver.maximize_window()
    yield firefox_driver
    firefox_driver.quit()


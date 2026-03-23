import pytest
from selenium import webdriver

@pytest.fixture(scope="function")

def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://v2.zenclass.in/login") #access zen portal page
    yield driver
    driver.quit() #exit browser
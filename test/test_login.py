import pytest
from Pages.login_page import LoginPage
from Pages.dashboard_page import DashboardPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Positive for successfull login
def test_login(driver):
    login = LoginPage(driver)
    dashboard = DashboardPage(driver)

    login.login("draj56403@gmail.com", "Ramesh@1#") #perform login
    dashboard.close_popup_if_present() #calls popup function if any popup present
    WebDriverWait(driver, 10).until(EC.url_contains("dashboard")) #wait until dashboard page load

    assert "dashboard" in driver.current_url #validate login success

#positive for login and logout
def test_logout_btn(driver):
    login = LoginPage(driver)
    dashboard = DashboardPage(driver)

    login.login("draj56403@gmail.com", "Ramesh@1#") #perform login

    dashboard.click_logout() #perform logout
    WebDriverWait(driver, 10).until(EC.url_contains("login")) #wait until login page load

    assert "login" in driver.current_url.lower() #validate logout is successfull

#negative test wrong credentials
def test_unsuccessful_login(driver):

    login = LoginPage(driver)
    login.login("draj5640", "Rames") #enter wrong credentials

    assert "*Incorrect email!" in driver.page_source #validates error message in the page

#positive check email and password field is displayed
def test_login_fields(driver):
    login = LoginPage(driver)

    assert driver.find_element(*login.user_name).is_displayed() #validates email field is displayed
    assert driver.find_element(*login.password).is_displayed() #validates password field is displayed

#positive check login button is enabled
def test_signup_btn(driver):
    login = LoginPage(driver)

    assert driver.find_element(*login.login_btn).is_enabled() #validates login button is enabled
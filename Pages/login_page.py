from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10) #Explicit wait

    user_name = (By.XPATH, "//input[@placeholder='Enter your mail']") #locator for email input field
    password = (By.XPATH, "//input[@placeholder='Enter your password ']") #locator for passport field
    login_btn = (By.XPATH, "//button[text()='Sign in']") #locator for login button

    def enter_username(self, user_name): #enter email function
        self.wait.until(EC.visibility_of_element_located(self.user_name)).send_keys(user_name)

    def enter_password(self, password): #function enter password
        self.wait.until(EC.visibility_of_element_located(self.password)).send_keys(password)

    def click_login_btn(self): #function click login button
        self.wait.until(EC.element_to_be_clickable(self.login_btn)).click()

    def login(self, user_name, password): #perform login actions
        try: #try and exception
            self.enter_username(user_name)
            self.enter_password(password)
            self.click_login_btn()
        except Exception as e:
            print("Login failed:", e)
            raise
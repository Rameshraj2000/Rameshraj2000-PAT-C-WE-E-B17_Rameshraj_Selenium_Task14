from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage: #class dashboard page
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    click_dropdown = (By.XPATH,"//img[@id='profile-click-icon']") #locator for dropdown to click logout
    logout_btn = (By.XPATH, "//div[contains(text(),'Log out')]") # locator for logout button
    close_popup_btn = (By.XPATH, "//button[@aria-label='Close popup']") # Locator for popup new app launch advert popup came

    def click_logout(self): #logout actions
        try: #try and exception
            self.close_popup_if_present()
            self.wait.until(EC.element_to_be_clickable(self.click_dropdown)).click()
            self.wait.until(EC.element_to_be_clickable(self.logout_btn)).click()
        except Exception as e:
            print("logout failed", e)
            raise

    def close_popup_if_present(self): # class to close popup if present in the page
        try: #try and except
            popup = self.wait.until(
                EC.element_to_be_clickable(self.close_popup_btn)
            )
            self.driver.execute_script("arguments[0].click();", popup)
            print("✅ Popup closed")
        except:
            print("⚠️ Popup not present")


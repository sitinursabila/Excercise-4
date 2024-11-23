import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class SauceDemo(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get('https://www.saucedemo.com/')
        self.assertIn("Swag Labs", self.browser.title)  # Perbaikan dari "Swag Lab" ke "Swag Labs"
      
    def test_login_b_failed(self):
        driver = self.browser
        driver.find_element(By.ID, 'user-name').send_keys("standard_user")
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret")
        driver.find_element(By.XPATH, "//input[@id='login-button']").click()
        
        # Perbaikan elemen untuk error message
        error_message = driver.find_element(By.CSS_SELECTOR, '[data-test="error"]').text
        self.assertIn("Username and password do not match", error_message)
  
    def test_login_a_success(self):
        driver = self.browser
        driver.find_element(By.ID, 'user-name').send_keys("standard_user")
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
        driver.find_element(By.XPATH, "//input[@id='login-button']").click()
        
        # Validasi URL setelah login berhasil
        get_url = driver.current_url
        self.assertIn('/inventory.html', get_url)  # URL dashboard SauceDemo
        
    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()

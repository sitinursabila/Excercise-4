import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DemoWebShopLogin(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get('https://demowebshop.tricentis.com/login')
        self.assertIn("Demo Web Shop. Login", self.browser.title)
        
    def test_login_success(self):
        driver = self.browser
        
        # Isi form login dengan data valid
        valid_email = "temp1@mail.com"  # Gunakan email yang valid
        valid_password = "123bila"  # Gunakan password yang valid
        driver.find_element(By.ID, 'Email').send_keys(valid_email)
        driver.find_element(By.ID, 'Password').send_keys(valid_password)
        driver.find_element(By.CSS_SELECTOR, 'input.login-button').click()
        
        # Tunggu sampai login berhasil dan verifikasi URL atau elemen setelah login
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'account'))
        )
        account_text = driver.find_element(By.CLASS_NAME, 'account').text
        self.assertEqual(account_text, valid_email)
    
    def test_login_failed(self):
        driver = self.browser
        
        # Isi form login dengan data tidak valid
        invalid_email = "invalid@example.com"
        invalid_password = "wrongpassword"
        driver.find_element(By.ID, 'Email').send_keys(invalid_email)
        driver.find_element(By.ID, 'Password').send_keys(invalid_password)
        driver.find_element(By.CSS_SELECTOR, 'input.login-button').click()
        
        # Verifikasi pesan error
        error_message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.message-error'))
        ).text
        self.assertIn("Login was unsuccessful", error_message)
    
    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()

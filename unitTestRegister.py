import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DemoWebShopRegister(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get('https://demowebshop.tricentis.com/register')
        self.assertIn("Demo Web Shop. Register", self.browser.title)

    def generate_dynamic_email(self):
        # Membuat email dinamis dengan timestamp
        timestamp = int(time.time())
        return f"user{timestamp}@example.com"
        
    def test_register_success(self):
        driver = self.browser
        dynamic_email = self.generate_dynamic_email()  # Email dinamis
        
        # Isi form registrasi dengan data valid
        driver.find_element(By.ID, 'gender-male').click()
        driver.find_element(By.ID, 'FirstName').send_keys("John")
        driver.find_element(By.ID, 'LastName').send_keys("Doe")
        driver.find_element(By.ID, 'Email').send_keys(dynamic_email)
        driver.find_element(By.ID, 'Password').send_keys("ValidPassword123")
        driver.find_element(By.ID, 'ConfirmPassword').send_keys("ValidPassword123")
        driver.find_element(By.ID, 'register-button').click()
        
        # Tunggu hingga URL beralih ke halaman hasil registrasi
        
        
        
        get_url = driver.current_url
        self.assertIn('result/1', get_url)
                    
          
    def test_register_failed(self):
        driver = self.browser
        
        # Isi form registrasi dengan data tidak valid
        driver.find_element(By.ID, 'gender-male').click()
        driver.find_element(By.ID, 'FirstName').send_keys("")
        driver.find_element(By.ID, 'LastName').send_keys("")
        driver.find_element(By.ID, 'Email').send_keys("invalid_email")
        driver.find_element(By.ID, 'Password').send_keys("short")
        driver.find_element(By.ID, 'ConfirmPassword').send_keys("mismatch")
        driver.find_element(By.ID, 'register-button').click()
        
        
        # Tunggu hingga pesan error muncul
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span.field-validation-error'))
        )
        
        # Verifikasi pesan error muncul pada halaman yang sama
        error_messages = driver.find_elements(By.CSS_SELECTOR, 'span.field-validation-error')
        self.assertGreater(len(error_messages), 0, "Pesan error tidak ditemukan")
        for message in error_messages:
            print("Error:", message.text)

    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()

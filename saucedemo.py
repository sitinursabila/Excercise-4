from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Menggunakan chrome option
#option = webdriver.ChromeOptions()
#option.add_experimental_option("detach", True)
#browser = webdriver.Chrome(options=option)

browser = webdriver.Firefox()
browser.get('https://www.saucedemo.com/')
assert 'Swag Labs' in browser.title

browser.find_element(By.ID, 'user-name').send_keys("standard_user")
browser.find_element(By.XPATH, "//input[@id='password']").send_keys("secret")
browser.find_element(By.XPATH, "//input[@id='login-button']").click()




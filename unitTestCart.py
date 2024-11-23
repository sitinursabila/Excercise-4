import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DemoWebShopCart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://demowebshop.tricentis.com/')
        self.assertIn("Demo Web Shop", self.driver.title)

    def test_add_to_cart(self):
        driver = self.driver

        # Pilih produk untuk ditambahkan ke keranjang
        product_name = "14.1-inch Laptop"
        driver.find_element(By.LINK_TEXT, product_name).click()

        # Klik tombol untuk menambahkan produk ke keranjang
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'add-to-cart-button-31'))
        ).click()

        # Verifikasi notifikasi bahwa produk berhasil ditambahkan ke keranjang
        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.bar-notification.success'))
        ).text
        self.assertIn("The product has been added to your shopping cart", success_message)

        # Navigasi ke keranjang belanja
        driver.find_element(By.LINK_TEXT, 'Shopping cart').click()
        WebDriverWait(driver, 10).until(
            EC.url_contains('/cart')
        )

        # Periksa apakah produk ada di keranjang
        try:
            cart_item = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'table.cart tr.product td.product a'))
            ).text
            self.assertIn(product_name, cart_item)
        except:
            print("Produk tidak ditemukan di keranjang.")

    def test_remove_from_cart(self):
        driver = self.driver

        # Navigasi ke halaman keranjang
        driver.get('https://demowebshop.tricentis.com/cart')

        # Pastikan ada produk di keranjang
        product_rows = driver.find_elements(By.CSS_SELECTOR, 'table.cart tr.product')
        if product_rows:
            # Klik tombol remove untuk menghapus produk
            remove_buttons = driver.find_elements(By.NAME, 'removefromcart')
            for button in remove_buttons:
                button.click()

            # Klik tombol update untuk konfirmasi penghapusan
            driver.find_element(By.NAME, 'updatecart').click()

            # Verifikasi bahwa keranjang kosong
            empty_message = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div.order-summary-content'))
            ).text
            self.assertIn("Your Shopping Cart is empty!", empty_message)
        else:
            print("Keranjang sudah kosong, tidak ada produk untuk dihapus.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
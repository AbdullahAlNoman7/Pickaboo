from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


class AddToCard(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        cls.driver.get("https://www.daraz.com.bd/")
        cls.wait = WebDriverWait(cls.driver, 30)

    def test_addTo_cart(self):
        self.driver.find_element(By.ID, "q").send_keys('Watches')
        self.driver.find_element(By.XPATH, "//button[normalize-space()='SEARCH']").click()
        self.driver.find_element(By.LINK_TEXT, "Men Business Watches").click()  # mens business watch
        self.driver.find_element(By.XPATH, "//span[normalize-space()='NAVIFORCE']").click()  # Naviforce
        # sort by
        self.driver.find_element(By.XPATH, "//div[@title='Best Match']").click()
        self.driver.find_element(By.XPATH, "//div[normalize-space()='Price high to low']").click()
        # select product
        self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "NAVIFORCE 1001 New Men's Mechanical Watches "
                                                                      "Wristwatch Stainless Steel "
                                                                      "Automatic ""Date Male Watch-Silver Blue"))).click()

    def test_abBuy_now(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"[data-spm-anchor-id='a2a0e\.pdp\.0\.i3"
                                                                    "\.1e49LzVaLzVagz']"))).click()
        """
        self.phone_number = self.driver.find_element(By.CSS_SELECTOR,".mod-login-input-loginName [type]")
        self.password = self.driver.find_element(By.CSS_SELECTOR,"[type='password']")
        self.assertTrue(self.phone_number.is_displayed(), True)
        self.phone_number.send_keys("01751437569")
        self.password.send_keys("123@adsf")
        """


if __name__ == "__main__":
    unittest.main()

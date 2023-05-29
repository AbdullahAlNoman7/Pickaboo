import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PickabooTest(unittest.TestCase):
    global driver

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        cls.driver.get("https://www.pickaboo.com/")
        cls.driver.implicitly_wait(5)
        cls.wait = WebDriverWait(cls.driver, 20)

    def test_01closeadd(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section[4]/div[3]/div[1]/img"))).click()
            self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section[5]/div/div/img"))).click()
        except:
            print("Element not found..")
        # self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="__next"]/section[1]/div[2]/div/div[3]/div[1]/div/a/span'))).click()

    @unittest.skip
    def test_02mousehover(self):
        self.mobile = self.driver.find_element(By.XPATH, "/html//div[@id='__next']/main/div/section[1]//div["
                                                         "@class='home-banner__menu']/div/ul//a["
                                                         "@href='/product/smartphone/']")
        self.iphone = self.driver.find_element(By.XPATH, "/html//div[@id='__next']/main/div/section[1]//div["
                                                         "@class='home-banner__menu']/div/ul/li[1]/ul["
                                                         "@class='has-sub']//a[@href='/product/iphone/']")
        self.action = ActionChains(self.driver)
        self.action.move_to_element(self.mobile).pause(2).click(self.iphone).pause(2).release().perform()

    @unittest.skip
    def test_0filter(self):
        self.driver.find_element(By.XPATH, "//span[@class='title-text']").click()
        self.driver.find_element(By.XPATH, "//ul/li[@innertext='Blue']").click()
        # sort by
        self.driver.find_element(By.XPATH, "//button[#'dropdown-basic']/p[@innertext='Default']").click()
        self.driver.find_element(By.LINK_TEXT, "Newest First").click()

    def test_02search(self):
        self.search = self.driver.find_element(By.XPATH,
                                               "//div[@class='menu-search col']//input[@placeholder='Search for "
                                               "products, brands and more']")
        self.search.send_keys("Mobile")
        self.driver.find_element(By.CSS_SELECTOR, "form > .btn.btn-primary").click()

    def test_03filter(self):
        self.driver.find_element(By.XPATH,
                                 "//span[normalize-space()='Category']//parent::button[@type='button']").click()
        self.driver.find_element(By.XPATH, "//li[contains(text(),'Smartphones')]").click()

    def test_04selectitem(self):
        self.select_item = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='OPPO F21s Pro 8GB/128GB']")))
        self.select_item.click()
        # add extra item
        self.color = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="__next"]/main/div/div/div/div/div[2]/div/div[6]/div[1]/div/div/center[1]/img')))
        self.color.click()
        time.sleep(2)
        self.sp = self.driver.find_element(By.XPATH, "//span[normalize-space()='Screen replacement + 1049']")
        self.sp.click()
        self.tws = self.driver.find_element(By.XPATH, "//span[normalize-space()='Lenovo LP40 TWS Earphone + 0']")
        self.tws.click()
        self.increment = self.driver.find_element(By.XPATH, "//div[@class='increment']//img")
        self.increment.click()
        time.sleep(2)
        # add to cart
        self.addto_cart = self.driver.find_element(By.XPATH, "//span[normalize-space()='ADD TO CART']")
        self.addto_cart.click()
        time.sleep(8)

    def test_05myCart(self):
        # click cart
        self.driver.find_element(By.XPATH, "//img[@alt='cart']").click()
        # apply discount
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Apply Discount Code']").click()
        self.discount_code = self.driver.find_element(By.XPATH, "//input[@placeholder='Enter Voucher Code']")
        self.discount_code.send_keys('B101')
        time.sleep(2)
        # self.driver.find_element(By.CSS_SELECTOR, ".show a").click()
        # user club coin
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Use Club Points']").click()
        self.club_coin = self.driver.find_element(By.XPATH, "//input[@placeholder='Enter amount of points to spend ']")
        self.club_coin.send_keys('105')
        time.sleep(2)


if __name__ == "__main__":
    unittest.main()

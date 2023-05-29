import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PickabooMouseAction(unittest.TestCase):
    global driver

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        cls.driver.get("https://www.pickaboo.com/")
        cls.driver.implicitly_wait(5)
        cls.wait = WebDriverWait(cls.driver, 20)

    def test_01closeadd(self):
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section[4]/div[3]/div[1]/img"))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section[5]/div/div/img"))).click()
        # self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="__next"]/section[1]/div[2]/div/div[3]/div[1]/div/a/span'))).click()

    def test_02mouseaction(self):
        time.sleep(10)
        self.sartphone = self.driver.find_element(By.XPATH, "//div[@class='home-banner__menu']//a[@class='a-tag']["
                                                            "normalize-space()='Smartphones']")
        # self.sartphone.click()
        self.iPhone = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/main[1]/div[1]/section[1]/div["
                                                         "1]/div[1]/div[1]/div[1]/ul[1]/li[1]/ul[1]/li[1]/a[1]")
        self.action = ActionChains(self.driver)
        self.action.move_to_element(self.sartphone).pause(2).click(self.iPhone).perform()


if __name__ == "__main__":
    unittest.main()

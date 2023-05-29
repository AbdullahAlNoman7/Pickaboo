from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time


class DarazLogin(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        cls.driver.get("https://www.daraz.com.bd/")
        cls.wait = WebDriverWait(cls.driver, 10)

    def test_login(self):
        self.singUp = self.driver.find_element(By.LINK_TEXT, "SIGNUP / LOGIN")
        self.singUp.click()
        print(self.driver.current_url)

    def test_register(self):
        self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Register"))).click()
        self.number = self.wait.until(EC.presence_of_element_located((By.XPATH,
                                                                      "//input[@placeholder='Please enter "                                                                       "your phone number']")))
        self.get_sms = self.driver.find_element(By.XPATH, "//span[@id='nc_2_n1z']")
        self.password = self.driver.find_element(By.CSS_SELECTOR, ".mod-login-input-password [type]")
        self.driver.find_element(By.XPATH, "//span[@id='month']//span[@class='next-select-placeholder']").click()
        self.month = self.driver.find_element(By.XPATH, '//li[text()="April"]')
        self.month.click()
        self.driver.find_element(By.XPATH, "//span[@id='day']//span[@class='next-select-placeholder']").click()
        self.days = self.driver.find_element(By.XPATH, "//li[text()='07']")
        self.days.click()
        self.driver.find_element(By.XPATH, "//span[@id='year']//span[@class='next-select-placeholder']").click()
        self.year = self.driver.find_element(By.XPATH, "//li[contains(text(),'1997')]")
        self.year.click()
        self.driver.find_element(By.XPATH, "//span[@id='gender']//span[@class='next-select-placeholder']").click()
        self.gender = self.driver.find_element(By.XPATH, "//ul//li[@value='male']")
        self.gender.click()
        self.username = self.driver.find_element(By.CSS_SELECTOR, ".mod-login-input-name [type]")
        self.sing_up = self.driver.find_element(By.XPATH, "//button[contains(text(),'SIGN UP')]")
        self.action = ActionChains(self.driver)
        self.number.send_keys('01751437569')
        self.action.drag_and_drop_by_offset(self.get_sms, 300, 0).pause(2).release().perform()
        self.password.send_keys('123456aa@')
        self.username.send_keys('Sagor')
        self.sing_up.click()
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div/div/div[1]/div[2]/div/div[1]/a/img").click()


    def test_saddto_cart(self):
        self.search = self.driver.find_element(By.ID,'q')
        self.search.send_keys('Watches')
        self.driver.find_element(By.XPATH,"//button[normalize-space()='SEARCH']").click()
        # category
        self.driver.find_element(By.LINK_TEXT,"Men Business Watches").click() # mens business watch
        self.driver.find_element(By.XPATH,"//span[normalize-space()='CURREN']").click() # Curren
        self.driver.find_element(By.XPATH,"//span[normalize-space()='NAVIFORCE']").click() # Naviforce
        # scroll
        self.scroll = self.driver.find_element(By.XPATH,"//div[normalize-space()='Location']")
        self.driver.execute_script("arguments[0].scrollIntoView;",self.scroll)
        self.driver.find_element(By.XPATH,"(//span[normalize-space()='China'])[1]").click() # china
        # price
        self.driver.find_element(By.XPATH,"//input[@placeholder='Min']").send_keys("1500")
        self.driver.find_element(By.XPATH,"//input[@placeholder='Max']").send_keys("5000")
        self.driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div[1]/div/div[2]/div/div[5]/div[2]/div/button").click()
        # watch color
        self.driver.find_element(By.XPATH,"//span[normalize-space()='Black']").click()
        # self.driver.find_element(By.XPATH,"//span[normalize-space()='Blue']").click()
        # self.driver.find_element(By.XPATH,"//span[normalize-space()='Silver']").click()
        time.sleep(2)
        # Strap Material
        # self.driver.find_element(By.XPATH,"//span[normalize-space()='Artificial Leather']").click()
        # select product



    @classmethod
    def tearDownClass(cls):
        # cls.driver.close()
        print("Tested...")


if __name__ == "__main__":
    unittest.main()

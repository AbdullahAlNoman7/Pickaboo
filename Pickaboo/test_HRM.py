import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait


class HRMLogin(unittest.TestCase):
    global driver

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        cls.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        cls.driver.implicitly_wait(5)
        cls.wait = WebDriverWait(cls.driver, 20)

    def test_01login(self):
        self.username = self.driver.find_element(By.NAME, "username")
        self.password = self.driver.find_element(By.NAME, "password")
        self.btn = self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
        # input data
        self.username.send_keys("Admin")
        self.password.send_keys("admin123")
        self.btn.click()
        self.assertEqual(self.driver.title, "OrangeHRM", "copmarision done")

    def test_02myinfo(self):
        self.driver.find_element(By.XPATH, "//span[normalize-space()='My Info']").click()
        self.driver.find_element(By.LINK_TEXT, "Personal Details").click()
        # Edit Info
        self.first_name = self.driver.find_element(By.NAME, "firstName")
        self.middle_name = self.driver.find_element(By.NAME, "middleName")
        self.last_name = self.driver.find_element(By.NAME, "lastName")
        self.nike_name = self.driver.find_element(By.XPATH, "//div[@class='orangehrm-horizontal-padding "
                                                            "orangehrm-vertical-padding']//div[1]//div[2]//div["
                                                            "1]//div[1]//div[2]//input[1]")
        self.emp_ID = self.driver.find_element(By.XPATH, "//div[@class='orangehrm-horizontal-padding "
                                                         "orangehrm-vertical-padding']//div[1]//div[2]//div[1]//div["
                                                         "1]//div[2]//input[1]")
        self.other_ID = self.driver.find_element(By.XPATH, "//div[@class='orangehrm-horizontal-padding "
                                                           "orangehrm-vertical-padding']//div[1]//div[2]//div[1]//div["
                                                           "1]//div[2]//input[1]")
        self.dl = self.driver.find_element(By.XPATH, "//div[@class='orangehrm-horizontal-padding "
                                                     "orangehrm-vertical-padding']//div[1]//div[2]//div[1]//div["
                                                     "1]//div[2]//input[1]")
        self.ssn_number = self.driver.find_element(By.XPATH, "//div[@class='orangehrm-horizontal-padding "
                                                             "orangehrm-vertical-padding']//div[1]//div[2]//div["
                                                             "1]//div[1]//div[2]//input[1]")
        self.sin_number = self.driver.find_element(By.XPATH, "//div[@class='orangehrm-horizontal-padding "
                                                             "orangehrm-vertical-padding']//div[1]//div[2]//div["
                                                             "1]//div[1]//div[2]//input[1]")
        self.nationality = self.driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(3) > div:nth-of-type(1) > "
                                                                     "div:nth-of-type(1) > "
                                                                     ".oxd-input-field-bottom-space.oxd-input-group "
                                                                     ".oxd-select-text")
        self.marital_status = self.driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(2) > "
                                                                        ".oxd-input-field-bottom-space.oxd-input-group"
                                                                        " .oxd-select-text > .oxd-select-text-input")
        self.dob = self.driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(3) > div:nth-of-type(2) > "
                                                             "div:nth-of-type(1) > "
                                                             ".oxd-input-field-bottom-space.oxd-input-group .oxd-input")
        self.gender = self.driver.find_element(By.XPATH, "//label[normalize-space()='Female']")
        self.military_status = self.driver.find_element(By.XPATH, "//div[@class='orangehrm-horizontal-padding "
                                                                  "orangehrm-vertical-padding']//div[1]//div[2]//div["
                                                                  "1]//div[1]//div[2]//input[1]")
        self.smoker = self.driver.find_element(By.XPATH, "//label[normalize-space()='Yes']")
        self.save_1 = self.driver.find_element(By.XPATH, "//div[@class='orangehrm-horizontal-padding "
                                                         "orangehrm-vertical-padding']//button[@type='submit']["
                                                         "normalize-space()='Save']")
        # Data
        if self.first_name.is_displayed() == True and self.first_name.is_enabled() == True:
            self.first_name.clear()
            self.first_name.send_keys("Hello")
        if self.middle_name.is_displayed() == True and self.middle_name.is_enabled() == True:
            self.middle_name.clear()
            self.middle_name.send_keys("Ketty")
        if self.last_name.is_displayed() == True and self.last_name.is_enabled() == True:
            self.last_name.clear()
            self.last_name.send_keys("Basfhj")
        if self.nike_name.is_displayed() == True and self.nike_name.is_enabled() == True:
            self.nike_name.clear()
            self.nike_name.send_keys("Meril")
        self.assertTrue(self.emp_ID.is_displayed(), True)
        self.emp_ID.clear()
        self.emp_ID.send_keys("105")
        self.assert_(self.other_ID.is_enabled(), True)
        self.other_ID.clear()
        self.other_ID.send_keys("124")
        self.assertTrue(self.dl.is_enabled(), True)
        self.dl.clear()
        self.dl.send_keys("2000")
        self.ssn_number.send_keys("3001")
        self.sin_number.send_keys("546")
        self.sel_nationality = Select(self.nationality)
        self.sel_nationality.select_by_value('5')
        self.sel_marit = Select(self.gender)
        self.sel_marit.select_by_value("3")
        self.assertEqual(self.gender.is_selected(), False)
        self.gender.click()
        self.marital_status.send_keys("789456")
        self.smoker.click()
        self.save_1.click()


if __name__ == "__main__":
    unittest.main()

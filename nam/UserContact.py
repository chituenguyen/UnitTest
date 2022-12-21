from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import HtmlTestRunner

class UserContact(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # using chrome in linux
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    @classmethod
    def setUp(self):
        self.driver.get("http://localhost/OnlinePizzaDelivery/index.php")
        time.sleep(2)
        self.driver.find_element(By.ID, "login").click()
        time.sleep(2)
        self.driver.find_element(By.NAME, "loginusername").send_keys("hoangnamqt")
        self.driver.find_element(By.NAME, "loginpassword").send_keys("123456")
        self.driver.find_element(By.ID,"submit").click()
        time.sleep(2)
        self.driver.get("http://localhost/OnlinePizzaDelivery/contact.php")
    @classmethod
    def tearDown(self):
        self.driver.get("http://localhost/OnlinePizzaDelivery/partials/_logout.php")
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Testing completed ...")

    def test_005_001_with_valid_contact_registration(self):
        # CLear field in phone input field
        self.driver.find_elements(By.NAME, "phone")[1].clear()
        self.driver.find_elements(By.NAME, "phone")[1].send_keys("0327453593")
        self.driver.find_elements(By.NAME, "password")[1].send_keys("123456")
        self.driver.find_element(By.NAME, "message").send_keys("May we help you")
        self.driver.find_elements(By.XPATH,"//button[@type='submit']")[3].click()
        time.sleep(2)
        text= self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        self.assertEqual("Thanks for Contact us." in text, True)

    def test_005_002_with_wrong_password_filed(self):
        # CLear field in phone input field
        self.driver.find_elements(By.NAME, "phone")[1].clear()
        self.driver.find_elements(By.NAME, "phone")[1].send_keys("0327453593")
        self.driver.find_elements(By.NAME, "password")[1].send_keys("1234")
        self.driver.find_element(By.NAME, "message").send_keys("May we help you")
        self.driver.find_elements(By.XPATH, "//button[@type='submit']")[3].click()
        time.sleep(2)
        text = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        self.assertEqual("Password incorrect!!", text)
    def test_005_003_with_empty_all_field(self):
        # CLear field in phone input field
        self.driver.find_elements(By.NAME,"email")[1].clear()
        self.driver.find_elements(By.NAME, "phone")[1].clear()
        self.driver.find_elements(By.NAME, "password")[1].clear()
        self.driver.find_elements(By.NAME, "orderId").clear()
        self.driver.find_elements(By.XPATH, "//button[@type='submit']")[3].click()
        time.sleep(2)
        current_url = self.driver.current_url
        self.assertEqual("http://localhost/OnlinePizzaDelivery/contact.php", current_url)
    def test_005_004_with_invalid_format_email(self):
        # CLear field in phone input field
        self.driver.find_elements(By.NAME, "email")[1].clear()
        self.driver.find_elements(By.NAME, "email")[1].send_keys("hoangnamqt.2015@")
        self.driver.find_elements(By.NAME, "phone")[1].clear()
        self.driver.find_elements(By.NAME, "phone")[1].send_keys("0327453593")
        self.driver.find_elements(By.NAME, "password")[1].send_keys("123456")
        self.driver.find_element(By.NAME, "message").send_keys("May we help you")
        self.driver.find_elements(By.XPATH, "//button[@type='submit']")[3].click()
        time.sleep(2)
        current_url = self.driver.current_url
        self.assertEqual("http://localhost/OnlinePizzaDelivery/contact.php", current_url)
    def test_005_005_with_message_have_length_255(self):
        # CLear field in phone input field
        self.driver.find_elements(By.NAME, "phone")[1].clear()
        self.driver.find_elements(By.NAME, "phone")[1].send_keys("0327453593")
        self.driver.find_elements(By.NAME, "password")[1].send_keys("123456")
        self.driver.find_element(By.NAME, "message").send_keys("aa")
        self.driver.find_elements(By.XPATH, "//button[@type='submit']")[3].click()
        time.sleep(2)
        current_url = self.driver.current_url
        self.assertEqual("http://localhost/OnlinePizzaDelivery/contact.php", current_url)

    def test_005_007_with_message_have_length_6(self):
            # CLear field in phone input field
            self.driver.find_elements(By.NAME, "phone")[1].clear()
            self.driver.find_elements(By.NAME, "phone")[1].send_keys("0327453593")
            self.driver.find_elements(By.NAME, "password")[1].send_keys("123456")
            self.driver.find_element(By.NAME, "message").send_keys("aaaaaaaa")
            self.driver.find_elements(By.XPATH, "//button[@type='submit']")[3].click()
            time.sleep(2)
            text = self.driver.switch_to.alert.text
            self.driver.switch_to.alert.accept()
            self.assertEqual("Thanks for Contact us." in text, True)
    def test_005_007_with_message_have_length_20(self):
        # CLear field in phone input field
        self.driver.find_elements(By.NAME, "phone")[1].clear()
        self.driver.find_elements(By.NAME, "phone")[1].send_keys("0327453593")
        self.driver.find_elements(By.NAME, "password")[1].send_keys("123456")
        self.driver.find_element(By.NAME, "message").send_keys("abcdefghikabcdefghik")
        self.driver.find_elements(By.XPATH, "//button[@type='submit']")[3].click()
        time.sleep(2)
        text = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        self.assertEqual("Thanks for Contact us." in text, True)
    def test_005_008_check_history_function(self):
        self.driver.find_element(By.XPATH,"//button[@data-target='#history']").click()
        time.sleep(2)
        text=self.driver.find_element(By.ID,"history").text
        self.assertEqual("Your Sent Message" in text, True)
    def test_005_009_check_history_function_after_submit(self):
        self.driver.find_elements(By.NAME, "phone")[1].clear()
        self.driver.find_elements(By.NAME, "phone")[1].send_keys("0327453593")
        self.driver.find_elements(By.NAME, "password")[1].send_keys("123456")
        self.driver.find_element(By.NAME, "message").send_keys("The dish is so messy")
        self.driver.find_elements(By.XPATH, "//button[@type='submit']")[3].click()
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        self.driver.get("http://localhost/OnlinePizzaDelivery/contact.php")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//button[@data-target='#history']").click()
        text=self.driver.find_element(By.ID,"history").text
        self.assertEqual("Your Sent Message" in text, True)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/pop_os_hi/Documents/HK221/Testing/Assigment3/Report'))

from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
import time


class AdminManageSite(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Edge()
        cls.driver.maximize_window()

    @classmethod
    def setUp(self):
        self.driver.get("http://localhost/OnlinePizzaDelivery/admin/login.php")
        time.sleep(2)
        self.driver.find_element(By.NAME, "username").send_keys("admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin")
        self.driver.find_element(By.NAME, "btn-login").click()
        self.driver.get("http://localhost/OnlinePizzaDelivery/admin/index.php?page=siteManage")

    @classmethod
    def tearDown(self):
        self.driver.get("http://localhost/OnlinePizzaDelivery/admin/partials/_logout.php")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Testing completed ...")

    def test_with_systemName_with_special_character(self):
        self.driver.find_element(By.NAME, "name").send_keys("@123.,")
        self.driver.find_element(By.NAME, "email").send_keys("user4@gmail.com")
        self.driver.find_element(By.NAME, "contact1").send_keys("09876543221")
        self.driver.find_element(By.NAME, "contact2").send_keys("09876543221")
        self.driver.find_element(By.NAME, "address").send_keys("tphcm")
        self.driver.find_element(By.NAME, "updateDetail").click()
        time.sleep(1)

        # check assign
        alert = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        self.assertEqual("success", alert)

    def test_with_systemName_without_special_character(self):
        self.driver.find_element(By.NAME, "name").send_keys("shopbro")
        self.driver.find_element(By.NAME, "email").send_keys("user4@gmail.com")
        self.driver.find_element(By.NAME, "contact1").send_keys("09876543221")
        self.driver.find_element(By.NAME, "contact2").send_keys("09876543221")
        self.driver.find_element(By.NAME, "address").send_keys("tphcm")
        self.driver.find_element(By.NAME, "updateDetail").click()
        time.sleep(1)

        # check assign
        alert = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        self.assertEqual("success", alert)

    def test_with_wrong_email(self):
        self.driver.find_element(By.NAME, "name").send_keys("shopbro")
        self.driver.find_element(By.NAME, "email").send_keys("user4gmail.com")
        self.driver.find_element(By.NAME, "contact1").send_keys("09876543221")
        self.driver.find_element(By.NAME, "contact2").send_keys("09876543221")
        self.driver.find_element(By.NAME, "address").send_keys("tphcm")
        self.driver.find_element(By.NAME, "updateDetail").click()
        time.sleep(1)

        # check assign
        current_url = self.driver.current_url
        self.assertEqual("http://localhost/OnlinePizzaDelivery/admin/index.php?page=siteManage", current_url)

    def test_with_true_email(self):
        self.driver.find_element(By.NAME, "name").send_keys("shopbro")
        self.driver.find_element(By.NAME, "email").send_keys("user4@gmail.com")
        self.driver.find_element(By.NAME, "contact1").send_keys("09876543221")
        self.driver.find_element(By.NAME, "contact2").send_keys("09876543221")
        self.driver.find_element(By.NAME, "address").send_keys("tphcm")
        self.driver.find_element(By.NAME, "updateDetail").click()
        time.sleep(1)

        # check assign
        alert = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        self.assertEqual("success", alert)

    def test_with_wrong_phone(self):
        self.driver.find_element(By.NAME, "name").send_keys("shopbro")
        self.driver.find_element(By.NAME, "email").send_keys("user4@gmail.com")
        self.driver.find_element(By.NAME, "contact1").send_keys("098765221")
        self.driver.find_element(By.NAME, "contact2").send_keys("09876543221")
        self.driver.find_element(By.NAME, "address").send_keys("tphcm")
        self.driver.find_element(By.NAME, "updateDetail").click()
        time.sleep(1)

        # check assign
        alert = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        self.assertEqual("error", alert)

    def test_with_phone_have_special_character(self):
        self.driver.find_element(By.NAME, "name").send_keys("shopbro")
        self.driver.find_element(By.NAME, "email").send_keys("user4@gmail.com")
        self.driver.find_element(By.NAME, "contact1").send_keys("09876asdf5221")
        self.driver.find_element(By.NAME, "contact2").send_keys("09876543221")
        self.driver.find_element(By.NAME, "address").send_keys("tphcm")
        self.driver.find_element(By.NAME, "updateDetail").click()
        time.sleep(1)

        # check assign
        alert = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        self.assertEqual("error", alert)

    def test_with_true_phone(self):
        self.driver.find_element(By.NAME, "name").send_keys("shopbro")
        self.driver.find_element(By.NAME, "email").send_keys("user4@gmail.com")
        self.driver.find_element(By.NAME, "contact1").send_keys("09876543221")
        self.driver.find_element(By.NAME, "contact2").send_keys("09876543221")
        self.driver.find_element(By.NAME, "address").send_keys("tphcm")
        self.driver.find_element(By.NAME, "updateDetail").click()
        time.sleep(1)

        # check assign
        alert = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        self.assertEqual("success", alert)

    def test_without_empty_address(self):
        self.driver.find_element(By.NAME, "name").send_keys("shopbro")
        self.driver.find_element(By.NAME, "email").send_keys("user4@gmail.com")
        self.driver.find_element(By.NAME, "contact1").send_keys("09876543221")
        self.driver.find_element(By.NAME, "contact2").send_keys("09876543221")
        self.driver.find_element(By.NAME, "address").send_keys("tphcm")
        self.driver.find_element(By.NAME, "updateDetail").click()
        time.sleep(1)

        # check assign
        alert = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        self.assertEqual("success", alert)


if __name__ == '__main__':
    unittest.main()

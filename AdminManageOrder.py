from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
import time


class AdminManageOrder(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Edge()
        cls.driver.maximize_window()

    @classmethod
    def setUp(self):
        self.driver.get("http://localhost/OnlinePizzaDelivery/admin/login.php")
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.get("http://localhost/OnlinePizzaDelivery/admin/partials/_logout.php")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Testing completed ...")

    def test_view_order_with_account_admin(self):
        self.driver.find_element(By.NAME, "username").send_keys("admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin")
        self.driver.find_element(By.NAME, "btn-login").click()
        time.sleep(5)
        # check assign
        self.driver.get("http://localhost/OnlinePizzaDelivery/admin/index.php?page=orderManage")
        nofication = self.driver.find_element(By.NAME, "order_detail")
        self.assertEqual("Order Details", nofication.text)

    def test_view_order_without_login(self):
        self.driver.get("http://localhost/OnlinePizzaDelivery/admin/index.php?page=orderManage")
        current_url = self.driver.current_url
        time.sleep(5)

        # check assign
        self.assertEqual("http://localhost/OnlinePizzaDelivery/admin/login.php", current_url)


if __name__ == '__main__':
    unittest.main()

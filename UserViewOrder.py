from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
import time


class ViewOrder(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Edge()
        cls.driver.maximize_window()

    @classmethod
    def setUp(self):
        self.driver.get("http://localhost/OnlinePizzaDelivery/index.php")
        time.sleep(5)
        self.driver.find_element(By.NAME, "btn_login").click()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.get("http://localhost/OnlinePizzaDelivery/partials/_logout.php")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Testing completed ...")

    def test_view_order_with_login_no_items(self):
        self.driver.find_element(By.NAME, "loginusername").send_keys("user1")
        self.driver.find_element(By.NAME, "loginpassword").send_keys("user1")
        self.driver.find_element(By.NAME, "btn_submit_login").click()
        time.sleep(5)
        # check assign
        self.driver.get("http://localhost/OnlinePizzaDelivery/viewOrder.php")
        nofication = self.driver.find_element(By.NAME, "order")
        self.assertEqual("You have not ordered any items.", nofication.text)

    def test_view_order_without_login(self):
        self.driver.get("http://localhost/OnlinePizzaDelivery/viewOrder.php")
        current_url = self.driver.current_url
        time.sleep(5)

        # check assign
        self.assertEqual("http://localhost/OnlinePizzaDelivery/partials/_loginModal.php", current_url)

    def test_view_order_with_login_have_items(self):
        self.driver.find_element(By.NAME, "loginusername").send_keys("user2")
        self.driver.find_element(By.NAME, "loginpassword").send_keys("user2")
        self.driver.find_element(By.NAME, "btn_submit_login").click()
        time.sleep(5)
        # check assign
        self.driver.get("http://localhost/OnlinePizzaDelivery/viewOrder.php")
        nofication = self.driver.find_element(By.NAME, "order_detail")
        self.assertEqual("Order Details", nofication.text)


if __name__ == '__main__':
    unittest.main()

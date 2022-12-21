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
        self.driver.get("http://localhost/OnlinePizzaDelivery/admin/login.php")
        time.sleep(2)
        self.driver.find_element(By.NAME, "username").send_keys("admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin")
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(2)
        self.driver.get("http://localhost/OnlinePizzaDelivery/admin/index.php?page=categoryManage")
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Testing completed ...")
    def test_006_001_create_with_valid_fields(self):
        self.driver.find_element(By.NAME, "name").send_keys("Susi")
        self.driver.find_element(By.NAME,"desc").send_keys("Very Delicious")
        self.driver.find_element(By.NAME,"image").send_keys('/home/pop_os_hi/Pictures/susi.jpg')
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(2)
        alert = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        self.assertTrue("success", alert)

    def test_006_002_create_with_invalid_name_fields(self):
        self.driver.find_element(By.NAME, "name").clear()
        self.driver.find_element(By.NAME, "name").send_keys("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        self.driver.find_element(By.NAME,"desc").clear()
        self.driver.find_element(By.NAME,"desc").send_keys("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb ")
        self.driver.find_element(By.NAME,"image").clear()
        self.driver.find_element(By.NAME,"image").send_keys('/home/pop_os_hi/Pictures/susi.jpg')
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(2)
        current_url = self.driver.current_url
        self.assertEqual("http://localhost/OnlinePizzaDelivery/admin/index.php?page=categoryManage", current_url)
    def test_006_003_create_with_blank_all_fields(self):
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(2)
        # check assign
        current_url = self.driver.current_url
        self.assertEqual("http://localhost/OnlinePizzaDelivery/admin/index.php?page=categoryManage", current_url)
    def test_006_004_create_with_only_name_catagery_invalid(self):
        self.driver.find_element(By.NAME, "name").send_keys("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        self.driver.find_element(By.NAME,"desc").send_keys("Very hot")
        self.driver.find_element(By.NAME,"image").send_keys('/home/pop_os_hi/Pictures/susi.jpg')
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(2)
        current_url = self.driver.current_url
        self.assertEqual("http://localhost/OnlinePizzaDelivery/admin/index.php?page=categoryManage", current_url)
    def test_006_005_create_with_only_description_blank(self):
        self.driver.find_element(By.NAME, "name").send_keys("Hot dog")
        self.driver.find_element(By.NAME,"desc").clear()
        self.driver.find_element(By.NAME,"image").send_keys('/home/pop_os_hi/Pictures/susi.jpg')
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(2)
        current_url = self.driver.current_url
        self.assertEqual("http://localhost/OnlinePizzaDelivery/admin/index.php?page=categoryManage", current_url)
    def test_006_006_create_category_with_only_namecategory_blank(self):
        self.driver.find_element(By.NAME, "name").clear()
        self.driver.find_element(By.NAME,"desc").send_keys("Very hot")
        self.driver.find_element(By.NAME,"image").send_keys('/home/pop_os_hi/Pictures/susi.jpg')
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(2)
        current_url = self.driver.current_url
        self.assertEqual("http://localhost/OnlinePizzaDelivery/admin/index.php?page=categoryManage", current_url)
    def test_006_007_check_delete_function(self):
        self.driver.find_element(By.NAME,"removeCategory").click()
        time.sleep(2)
        alert = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        self.assertTrue("Removed", alert)
    def test_006_008_check_especial_input(self):
        self.driver.find_element(By.NAME, "name").send_keys("<scrip>window.location.href='http://www.google.com'</script>")
        self.driver.find_element(By.NAME,"desc").send_keys("Very hot")
        self.driver.find_element(By.NAME,"image").send_keys('/home/pop_os_hi/Pictures/susi.jpg')
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(2)

        current_url = self.driver.current_url
        self.assertEqual("http://localhost/OnlinePizzaDelivery/admin/index.php?page=categoryManage", current_url)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/pop_os_hi/Documents/HK221/Testing/Assigment3/Report'))

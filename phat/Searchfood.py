import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class Searchfood(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost/OnlinePizzaDelivery/")
        
    def test_food_in_menu_when_logged(self,foodname = 'PANEER MAKHANI'):
        self.loggintoapp()
        self.driver.find_element(By.ID, 'search').send_keys(foodname)
        self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-outline-success.my-2.my-sm-0").click()
        lstOfFoods = self.driver.find_elements(By.CSS_SELECTOR, 'h5.card-title')
        temp = []
        for food in lstOfFoods:
            temp.append(food.text[0:5])
        self.assertIn(foodname[0:5],temp)
        
    def test_food_not_in_menu_when_logged(self,foodname = 'bun dau cham man tom'):
        self.loggintoapp()
        self.driver.find_element(By.ID, 'search').send_keys(foodname)
        self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-outline-success.my-2.my-sm-0").click()
        # div = self.driver.find_elements(By.CSS_SELECTOR, '.container h1')
        time.sleep(1)
        a = self.driver.find_elements(By.TAG_NAME, 'h1')[0].text
        self.assertIn('No Result Found',a)
        
    def test_when_not_input_when_logged(self):
        self.loggintoapp()
        self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-outline-success.my-2.my-sm-0").click()
        result = self.driver.find_elements(By.CSS_SELECTOR, "h2.py-2")
        self.assertEqual([],result)

        
    def test_food_in_menu_when_not_log(self,foodname = 'PANEER MAKHANI'):
        self.driver.find_element(By.ID, 'search').send_keys(foodname)
        self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-outline-success.my-2.my-sm-0").click()
        lstOfFoods = self.driver.find_elements(By.CSS_SELECTOR, 'h5.card-title')
        temp = []
        for food in lstOfFoods:
            temp.append(food.text[0:5])
        self.assertIn(foodname[0:5],temp)
        
    def test_food_not_in_menu_when_not_log(self,foodname = 'bun dau cham man tom'):
        self.driver.find_element(By.ID, 'search').send_keys(foodname)
        self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-outline-success.my-2.my-sm-0").click()
        # div = self.driver.find_elements(By.CSS_SELECTOR, '.container h1')
        time.sleep(1)
        a = self.driver.find_elements(By.TAG_NAME, 'h1')[0].text
        self.assertIn('No Result Found',a)  
        
    def test_when_not_input_when_not_log(self):
        self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-outline-success.my-2.my-sm-0").click()
        result = self.driver.find_elements(By.CSS_SELECTOR, "h2.py-2")
        self.assertEqual([],result)            


      

    
    def loggintoapp(self):
        self.findLoginbtn().click()
        self.driver.find_element(By.ID, 'loginusername').send_keys("user1")
        self.driver.find_element(By.ID, 'loginpassword').send_keys("user1")
        for sub in self.findsubmitlogin():
            if sub.text == 'Submit':
                sub.click()
                break 
            
    def findsubmitlogin(self):
        return self.driver.find_elements(By.CSS_SELECTOR, ".btn.btn-success")            
    
    def findLoginbtn(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#navbarSupportedContent .btn.btn-success.mx-2")    
    
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()    
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class LoginFeature(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost/OnlinePizzaDelivery/")     

    def test_login_username_true_password_wrong(self): 
        if self.accessOk():            
            self.findLoginbtn().click()            
            self.driver.find_element(By.ID, 'loginusername').send_keys("user1")
            self.driver.find_element(By.ID, 'loginpassword').send_keys("u@@@@@@@@ser1")
            time.sleep(1)
            for sub in self.findsubmitlogin():
                if sub.text == 'Submit':
                    sub.click()
                    break                    
           
            warningstring = 'Warning! Invalid Credentials' if  self.driver.find_elements(By.CSS_SELECTOR,".alert.alert-warning.alert-dismissible.fade.show") else 'false'
            self.assertIn('Warning', warningstring)
            
            
    def test_login_not_enter_username(self): 
        if self.accessOk():            
            self.findLoginbtn().click()            
            # self.driver.find_element(By.ID, 'loginusername').send_keys("u2ser1")
            self.driver.find_element(By.ID, 'loginpassword').send_keys("user1")
            time.sleep(1)
            for sub in self.findsubmitlogin():
                if sub.text == 'Submit':
                    sub.click()
                    e = self.driver.find_element(By.ID, 'loginusername').get_attribute("required")
                    break 
            # print(e)
            self.assertEqual(e,"true")
            
            
    def test_login_not_enter_password(self): 
        if self.accessOk():            
            self.findLoginbtn().click()            
            self.driver.find_element(By.ID, 'loginusername').send_keys("user1")
            # self.driver.find_element(By.ID, 'loginpassword').send_keys("user1")
            time.sleep(1)
            for sub in self.findsubmitlogin():
                if sub.text == 'Submit':
                    sub.click()
                    e = self.driver.find_element(By.ID, 'loginpassword').get_attribute("required")
                    break 
            # print(e)
            self.assertEqual(e,"true")
            
            
            
    def test_login_success(self): 
        # having username : user1 and password: user1 in database
        if self.accessOk():            
            self.findLoginbtn().click()            
            self.driver.find_element(By.ID, 'loginusername').send_keys("user1")
            self.driver.find_element(By.ID, 'loginpassword').send_keys("user1")
            time.sleep(1)
            for sub in self.findsubmitlogin():
                if sub.text == 'Submit':
                    sub.click()
                    break 
        succ = 'true' if  self.driver.find_elements(By.CSS_SELECTOR,".rounded-circle") else 'false'
        self.assertEqual(succ,"true")
            

    def findsubmitlogin(self):
        return self.driver.find_elements(By.CSS_SELECTOR, ".btn.btn-success")
        
    def accessOk(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".navbar-brand").text == 'Pizza World'
    
    def findLoginbtn(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#navbarSupportedContent .btn.btn-success.mx-2")
        
        

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()        
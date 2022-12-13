import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class LoginFeature(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost/OnlinePizzaDelivery/")

    def test_login_in_python(self):    
        if self.accessOk():            
            self.findLoginbtn().click()            
            self.driver.find_element(By.ID, 'loginusername').send_keys("usser1")
            self.driver.find_element(By.ID, 'loginpassword').send_keys("user1")
            time.sleep(1)
            for sub in self.findsubmitlogin():
                if sub.text == 'Submit':
                    sub.click()
                    break                    
            # time.sleep(2)

            
            warningstring = 'Warning! Invalid Credentials' if  self.driver.find_elements(By.CSS_SELECTOR,".alert.alert-warning.alert-dismissible.fade.show") else 'true'
            self.assertNotIn('Warning', warningstring)
            

                                 
        return False

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
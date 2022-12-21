# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestManageProfile():
  def setup_method(self, method):
    self.driver = webdriver.Chrome(executable_path="C:/Users\Public/chromedriver_win32/chromedriver.exe")
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_manageProfile(self):
    self.driver.get("http://localhost/OnlinePizzaDelivery-main/OnlinePizzaDelivery-main/OnlinePizzaDelivery/viewProfile.php")
    self.driver.set_window_size(1536, 824)
    self.driver.find_element(By.CSS_SELECTOR, "form:nth-child(2) #firstName").click()
    self.driver.find_element(By.CSS_SELECTOR, "form:nth-child(2) #firstName").send_keys("")
    self.driver.find_element(By.NAME, "updateProfileDetail").click()
    self.driver.find_element(By.CSS_SELECTOR, "form:nth-child(2) #firstName").send_keys("user2")
    self.driver.find_element(By.CSS_SELECTOR, "form:nth-child(2) #lastName").click()
    self.driver.find_element(By.CSS_SELECTOR, "form:nth-child(2) #lastName").send_keys("yt")
    self.driver.find_element(By.NAME, "updateProfileDetail").click()
    self.driver.find_element(By.CSS_SELECTOR, "form:nth-child(2) #email").click()
    self.driver.find_element(By.CSS_SELECTOR, "form:nth-child(2) #email").send_keys("user")
    self.driver.find_element(By.CSS_SELECTOR, "form:nth-child(2) #email").send_keys("@gmail")
    self.driver.find_element(By.NAME, "updateProfileDetail").click()
    self.driver.find_element(By.CSS_SELECTOR, "form:nth-child(2) #email").click()
    self.driver.find_element(By.CSS_SELECTOR, "form:nth-child(2) #email").send_keys("user@gmail")
    self.driver.find_element(By.CSS_SELECTOR, ".col-md-6 > .mb-3").click()
    self.driver.find_element(By.CSS_SELECTOR, ".col-md-6 #phone").send_keys("")
    self.driver.find_element(By.NAME, "updateProfileDetail").click()
    self.driver.find_element(By.CSS_SELECTOR, ".col-md-6 #phone").send_keys("123abc")
    self.driver.find_element(By.NAME, "updateProfileDetail").click()
    self.driver.find_element(By.CSS_SELECTOR, ".col-md-6 #phone").send_keys("1111111111")
    self.driver.find_element(By.NAME, "updateProfileDetail").click()
    self.driver.find_element(By.CSS_SELECTOR, ".form-group #password").send_keys("adsfsafsaf")
    self.driver.find_element(By.NAME, "updateProfileDetail").click()
    self.driver.find_element(By.CSS_SELECTOR, ".form-group #password").click()
    self.driver.find_element(By.CSS_SELECTOR, ".form-group #password").send_keys("1234567")
    self.driver.find_element(By.NAME, "removeProfilePic").click()
    self.driver.find_element(By.ID, "image").click()
    self.driver.find_element(By.ID, "image").send_keys("C:\\fakepath\\adjustitem.PNG")
    self.driver.find_element(By.NAME, "updateProfilePic").click()
    self.driver.find_element(By.ID, "loginusername").send_keys("user2")
    self.driver.find_element(By.NAME, "removeProfilePic").click()
    self.driver.find_element(By.CSS_SELECTOR, ".form-group #password").send_keys("1234567")
    self.driver.find_element(By.NAME, "updateProfileDetail").click()
    self.driver.find_element(By.CSS_SELECTOR, "a:nth-child(1) > .btn").click()
    element = self.driver.find_element(By.LINK_TEXT, "Contact Us")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
  

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest,time,re

class Case01(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url="https://www.katalon.com/"
        self.accept_next_alert=True

    def test_case01(self):
        driver=self.driver
        driver.get("https://www.so.com")
        driver.find_element_by_id("input").click()
        driver.find_element_by_id("input").clear()
        driver.find_element_by_id("input").send_keys(u"肯德基")
        driver.find_element_by_id("search-button").click()
        self.assertEqual(u"肯德基",
driver.find_element_by_id("keyword").get_attribute("value"))

mytest=Case01()
mytest.setUp()
mytest.test_case01()


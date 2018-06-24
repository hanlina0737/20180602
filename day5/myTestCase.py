#在myTestCase中,封装setup和tearDown方法,达到一劳永逸的作用
import unittest
from selenium import webdriver
import time

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        # time.sleep(30)
        cls.driver.quit()
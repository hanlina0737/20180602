import unittest

import time
from selenium import webdriver
import pymysql
from selenium.webdriver.common.by import By

from day5.myTestCase import MyTestCase
from day6.DBconnection import DBConnection


class RegisterTest(MyTestCase):
    def test_register(self):
        # 1.数据库验证,测试的正常情况
        driver = self.driver
        self.driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        driver.find_element(By.NAME, 'username').send_keys("士大夫3")
        driver.find_element(By.NAME, 'password').send_keys("123456")
        driver.find_element(By.NAME, 'userpassword2').send_keys("123456")
        driver.find_element(By.NAME, 'mobile_phone').send_keys("18699865432")
        driver.find_element(By.NAME, 'email').send_keys("456872@qq.com")
        driver.find_element(By.CLASS_NAME, 'reg_btn').click()
        time.sleep(3)

        new_record = DBConnection().excute_sql_commond()
        self.assertEqual("士大夫3",new_record[1])
        self.assertEqual("456872@qq.com",new_record[2])
        print(new_record)
#
# if __name__ == '__main__':
#     RecursionError().test_regesiter()
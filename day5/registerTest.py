# 1.导包
import unittest

import time
from selenium import webdriver
# 继承unittest.testcase
from selenium.webdriver.common.by import By

from day5.csvFileManager4 import CsvFileManager4


class RegisterTest(unittest.TestCase):
    # 3.重写setup 和 tearDown 方法
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    @classmethod
    def tearDownClass(cls):
        time.sleep(30)
        cls.driver.quit()
        # close是关闭一个标签页,quit是关闭一个浏览器,所以窗口切换的时候是用close
        # 4.编写一个测试用例的方法(以test开头的方法)
    def test_register(self):
        for row in CsvFileManager4().read('test_data.csv'):

            driver = self.driver
            driver.get("http://localhost/index.php?m=user&c=public&a=reg")
            driver.find_element(By.NAME,'username').send_keys(row[0])
            #driver.find_element_by_name()与上边的一样,没有任何区别,但是第一种方法扩展性更好,便于我们的框架封装
            driver.find_element(By.NAME,'password').send_keys(row[1])
            driver.find_element(By.NAME,'userpassword2').send_keys(row[2])
            driver.find_element(By.NAME,'mobile_phone').send_keys(row[3])
            driver.find_element(By.NAME,'email').send_keys(row[4])

            driver.find_element(By.CLASS_NAME,'reg_btn').click()

# 在for循环中执行测试用例,虽然解决批量执行的问题,但是如果第一行测试用例执行失败,后续的测试用例还会不会执行
# 异常情况,输入完邮箱后,按tab键,检查提示信息是否都是通过信息验证状态
# 如果页面上提示的心事是通过信息验证,那么就认为测试用例成功了,否则失败
            check_tip = driver.find_element(By.CSS_SELECTOR,'body > div.w1180 > div > div.reg_main > div.reg_left.fl > form > ul > li:nth-child(6) > p > input').text
            # 断言写法
            self.assertEqual("请输入",check_tip)
# 虽然第一行测试数据执行失败了,但是后面的测试数据是不依赖于前面的,不应该因为第一条失败就导致其他航数据不执行测试
#所以不应该用for循环的方式执行不同的测试数据,因为在方法中写了for循环虽然执行了多次,但是unittest仍然认为它是一条测试用例,一旦断言失败就会终止这条测试用例
#
#             print(check_tip)
#             # 其中check_tip是执行用例时,从网页上抓取信息
#             # "通过信息验证"是来自于手工测试用例,是测试用例执行前的期望结果
#             if check_tip == "通过信息验证!":
#                 print("ok")
#             else:
#                 print("fail")
# #                 这样通过if...else语句就可以自动判断测试用例的执行情况

if __name__ == '__main__':
    unittest.main()

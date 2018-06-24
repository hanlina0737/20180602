import unittest

import time

from selenium.webdriver.common.by import By

from day5.myTestCase import MyTestCase
from day5.page_object.loginPage import LoginPage
from day5.page_object.memberCenterPage import MemberCenterPage


class LoginTest2(MyTestCase):
    # 这时,这个类不需要在写setUP和tearDown方法了,
# 只需要写测试用例方法即可
    def test_login(self):
        # deriver = self.driver
        # deriver.get("http://localhost/index.php?m=user&c=public&a=login")
        # deriver.find_element_by_name("username").send_keys("fanxiao")
        # deriver.find_element_by_id("password").send_keys("111111")
        # deriver.find_element_by_class_name("login_btn").click()
        # time.sleep(5)
        # # 通过判断导航栏中是否存在用户名,从而判断登录是否成功
        # welcomeTxt = deriver.find_element(By.PARTIAL_LINK_TEXT,"您好").text
        # # 断言
        # self.assertEqual(welcomeTxt,"您好 fanxiao")
        # 现在这个测试用例把元素定位这样的技术问题和手工测试用例的业务逻辑混合在一个文件中,不利于后期维护,我们应该分层处理,有的文件只处理业务逻辑,有的文件只处理元素定位
        # 我们这是一个测试用例类,应该只包含测试用例的业务逻辑,把元素定位单独放在其他文件中
        # 1.打开登录页面
        # 要想调用login_page类中封装好的open(),首先必须实例化login_page的对象
        login_page = LoginPage(self.driver)
        login_page.open()
        # 2.输入用户名
        login_page.input_username()
        # 3.输入密码
        login_page.input_password()
        # 4.点击登录按钮
        login_page.click_login_button()
        # 5.在会员中心页面验证用户名是否显示正确
        member_center_page = MemberCenterPage(self.driver)
        self.assertEqual(member_center_page.get_welcome_link_text(),"您好,fanxiao")
        # 应该把代码写成和手工测试用例一样的感觉
        # 这样别人看你的代码就知道你的业务逻辑是否正确

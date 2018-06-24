#这种框架的设计思想叫做page-object设计模式,是一种高级的框架设计思想
# 这种思想的主旨是把业务逻辑和代码技术分离开
# 测试用例的类,专门负责业务逻辑
# 定位元素和操作交给网页对象类
# 在page_object这个类中,把每个网页看成一个类,其中 网页中的每个元素看成类中的一个属性
# 针对这个元素的操作看成类中的一个方法
# 元素的信息定位是名词性的所以看成属性(成员变量),元素的操作是动词性的所以是看成方法
# 那么下面我们封装以下登录这个网页
# 这个类主要做的就是把元素定位改一个易于理解的名字
# deriver.get("http://localhost/index.php?m=user&c=public&a=login")
# deriver.find_element_by_name("username").send_keys("fanxiao")
# deriver.find_element_by_id("password").send_keys("111111")
# deriver.find_element_by_class_name("login_btn").click()
# 把上面的代码封装成下面的样子
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
#     给类这个网页创建一个构造函数
# 在python中过早函数固定名字__init__()
    def __init__(self,driver):
        # 因为setup方法中已经创建了一个浏览器,
        # 所以这里不需要新建浏览器,直接用setup建立好的浏览器
        # self.driver = webdriver.Chrome()
        self.driver = driver
        self.url = "http://localhost/index.php?m=user&c=public&a=login"
    # 声明一个变量username_input_loc,保存元素的定位方式
    # 这句话的意思是声明了一个数组叫username_input_loc
    # 数组中有两个元素分别是ID,"username"
    username_input_loc = (By.ID,"username")
    password_input_loc = (By.ID,"password")
    login_button_loc = (By.CLASS_NAME,"login_btn")
    def open(self):
        self.driver.get(self.url)
    # username="fanxiao" 给参数设置默认值,如果调用方法时,传入一个新的用户名,那么使用新的,
    # 如果调用方法是不传参那么使用默认值
    def input_username(self,username="fanxiao"):
        # 这个类中涉及到三个元素定位,因为元素定位不太稳定,经常需要修改,所以应该把定位方式声明成类中的一个属性
        # self.driver.find_element(By.ID,"username").send_keys(username)
        # *表示给find_element这个方法传入的不是一个列表,而是把元组中的每个元素都分别传入find_element这个方法作为单独参数
        self.driver.find_element(*self.username_input_loc).send_keys(username)
    def input_password(self,password = "111111"):
        self.driver.find_element(*self.password_input_loc).send_keys(password)
    def click_login_button(self):
        self.driver.find_element(*self.login_button_loc).click()


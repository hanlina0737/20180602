#这个文件用来实现一个登录功能的自动化操作
import time
from selenium import webdriver   #从  谷歌公司的一个项目  导入  网络驱动,用来操作浏览器的

#1.打开浏览器
driver = webdriver.Chrome()

# 设置智能等待
driver.implicitly_wait(20) #设置隐式等待,一旦找不到页面元素,马上执行后面的语句,如果超过20s找不到页面元素,那么程序将会报错,超时错误

# 2.打开海盗商城网站
driver.get("http://172.31.15.27:8081/")
# 3.打开登录页面
driver.get("http://172.31.15.27:8081/index.php?m=user&c=public&a=login")
# 4.输入用户名和密码
driver.find_element_by_id("username").send_keys("fan")
driver.find_element_by_id("password").send_keys("123456")
# 5.点击登录按钮
# 所有调用方法都会有 提示信息,没有提示信息,就说明没有这个方法
driver.find_element_by_class_name("login_btn").click()
# 6.检查登录是否成功
#time.sleep(5) #导包的快捷键 alt+enter 选import this name,选最短的time
# time.slepp()这个方法提供了一种固定的时间等待
# 这里的意义是点击登录按钮后,等5秒后在检查用户名是否正常显示
# 弊端不知道到底等多少秒合适,因为网络延迟不知道每次等待时间设置多长合适
# 解决办法是用只能等待代替固定的时间等待

username_text = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[2]/a[1]").text
print(username_text)

#我们可以通过if语句判断页面显示的文本和预期的文本是否一致,来判断测试用例是否正常执行
if username_text == "您好 fan":
    print("pass")
else:
    print("error")
#因为selenium主要做回归测试,所以测试脚本刚开始都是pass的.只有开发做了代码变更,我们的测试用例才有可能失败
# 一般工作中 不用if else 做判断,之后详细讨论此问题

# 点击"进入商城购物"
# driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/dl[1]/dd/div/p/a").click()
driver.find_element_by_link_text("进入商城购物").click()
#8. 在商城主页输入搜索条件iPhone
driver.find_element_by_name("keyword").send_keys("iphone")
# 9.点击搜索按钮
driver.find_element_by_class_name("btn1").click()
# 10.在搜索结果页面点击第一个商品图片
driver.find_element_by_link_text("苹果 (Apple) iPhone 6 (A1586) 16GB 金色 移动联通电信4G手机").click()
# 11.加入购物车
# 窗口切换
driver.close()#关闭selenium正在工作的窗口
all_handles = driver.window_handles
driver.switch_to.window(all_handles[-1])
driver.find_element_by_id("joinCarButton").click()
import time
from selenium import webdriver

# 文件名,类名,包名,都应该以字母开头,可以有数字和下划线,但是不能用空格和中文
from day02.loginTest import Login

# 实例化对象会占用内存,pycharm会自动帮我们做释放内存
# 代码运行完检测到login()这个对象不再被使用,系统会自动释放内存
# 把driver浏览器传入到登录方法中
# 让登录方法和下面的点击账号使用的是同一个浏览器
# 我们已经创建好一个空白的浏览器了,后续的所有操作都应该在这个浏览器上执行
driver = webdriver.Chrome()
# 每次创建浏览器时,固定写一次隐式等待,对在这个浏览器的执行的所有代码都生效
# implicitly_wait()主要是监测页面的加载时间,检测什么时候页面加载完,什么时候执行后续的操作
driver.implicitly_wait(20)

Login().loginWithDefaultUser(driver)
# 1.登录海盗商城
# driver.get("http://172.31.15.27:8081/index.php?m=user&c=public&a=login")
# driver.find_element_by_name("username").send_keys("fan")
# driver.find_element_by_id("password").send_keys("123456")
# driver.find_element_by_class_name("login_btn").click()
# 2.点击账号设置
# 本来点击  账号设置,需要使用driver这个变量,现在文件中没有driver 变量了怎么办
# 可以重新声明一个driver吗?nono
driver.find_element_by_xpath("/html/body/div[2]/div[4]/div/ul/li[1]/a").click()
# 3.点击 个人资料
driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[4]/ul/li[2]/a").click()
# partial_link_text可以使用链接的一部分进行元素定位当链接文本过长时推荐使用
# 使用partial_link_text时可以用链接中任意部分,保证是唯一的就可以
# driver.find_element_by_partial_link_text("个料").click()
# 4.修改真实姓名
# 如果输入框中原本有内容,那么我门修改内容是,往往需要先清空原来的值,用clear方法
# 实际上一个良好的编程习惯是在每次send_keys之前都先做clear操作
driver.find_element_by_class_name("input_2").clear()
driver.find_element_by_class_name("input_2").send_keys("樊樊樊")

# 5.修改性别
# 通过观察,发现保密 男 女 三者唯一的区别就是value属性的值
# 我们可以通过value的属性来定位么?  可以
# 实际上我们可以通过任何的属性来定位
# 要想通过value属性定位有两种方法"XPath css_selector
# 通过css_selector定位元素,只需要在唯一属性的两边加一对中括号即可
# driver.find_element_by_css_selector("[value='2']").click()
# 在XPath中//表示采用相对路径定位元素
# /表示绝对路径,一般都是从/html根节点开始定位元素
# 相对路径一般通过元素的特殊属性查找元素
# 绝对路径一般通过元素的位置,层级关系查找元素
# 绝对路径写起来比较长,涉及到的节点比较多,当开发人员修改页面布局时,受到影响的可能性比较大
# 相对路径,查询速度比较慢,因为可能需要遍历更多的节点,同样找一个元素用绝对路径的速度会快一些
# 工作中推荐用css_selector,它的查询速度比XPath快一点,XPath在某些浏览器上支持的不调和,比如ie8
# css_selector所有前端开发都会用,易于沟通交流
# *星号表示任意节点
# [@]表示通过属性定位
# javascript的getElementsByClassName()方法可以找到页面上符合条件的所有元素
# 然后下标选取其中第n个元素,也可以用于定位,对不对?
# selenium可不可以用这种思路来定位元素?
# 要想找页面上所有元素就要用elements 唯一元素就用element
driver.find_elements_by_id("xb")[2].click()

# driver.find_element_by_xpath('//*[@value="2"]').click()
# 6.修改生日
driver.execute_script('document.getElementById("date").removeAttribute("readonly")')
driver.find_element_by_id("date").clear()
driver.find_element_by_id("date").send_keys("1990-05-20")
# 7.修改qq
driver.find_element_by_id("qq").clear()
driver.find_element_by_id("qq").send_keys("888899456")
# 8.点击确定,保存成功
driver.find_element_by_class_name("btn4").submit()
time.sleep(3)
# 确定
driver.switch_to.alert().accept()
# 取消
# driver.switch_to.alert().dismiss()
# 注意 这是一个JavaScript控件,它的出现不会造成页面重新加载,所以implicitly_wait()对alert弹出的所需的时间等待是无效的,所以在执行alert操作前,需要加一个固定的,一般是3s的时间等待
# 因为alert出现是需要延时的
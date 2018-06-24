# selenium执行javascript中的两个关键字: return(返回值) 和 arguments(参数)
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("http://localhost")
driver.implicitly_wait(20)
# 点击"登录"链接
# 用javascript的方法找登录链接的代码:
# document.getElementsByClassName("site-nav-right fr")[0].childNodes[1]
# 用selenium的方法找登录链接的代码:
# driver.find_element_by_link_text("登录")
# 通常,用selenium的方法找元素比javascript更容易
# 虽然selenium 不支持remoceAttribute的javascript方法
# 但是selenium找到登录链接和javascript找到的是同一个元素
# 我们可不可以把selenium找到的这个元素,传入到javascript方法里,代替原来的javascript定位
login_link = driver.find_element_by_link_text("登录")
# arguments参数的复数形式, [0]表示第一个参数,指的就是js后面的login_link
# 所以下面这句代码,相当于把driver.find_element_by_link_text("登录")带入到javascript语句中
# 变成了driver.find_element_by_link_text("登录").removeAttribute('target')
# arguments是参数数组,指的是js字符串后面的所有参数
# 一般情况下我们只会用到argument[0],即js后面的第一个字符串
driver.execute_script("arguments[0].removeAttribute('target')", login_link)
login_link.click()
# 执行成功的自己写登录
driver.find_element_by_id("username").send_keys("changcheng")
ActionChains(driver).send_keys(Keys.TAB).send_keys("123654").send_keys(Keys.ENTER).perform()
# 返回商城首页
driver.find_element_by_link_text("进入商城购物").click()
# 搜索iphone
driver.find_element_by_name("keyword").send_keys("iphone")
driver.find_element_by_name("keyword").submit()
# 点击商品(用这种方法,再实现一次不打开新窗口)
# 使用javascript删除a标签的target属性
# 因为img没有target属性,所以我们复制css的时候要找它的父节点a标签
# 复制出来的css往往比较长,我们可以适当的缩写长度
# 我们定位元素的目标节点是最后一个节点,
# 大于号>的前面是父节点,后面是子节点
# 每个节点的第一个单词是标签名,比a,div,body
# 小数点后面表示class属性
# :nth-child(2), nth表示第几个4th,5th,nth表示第n个, child表示子节点
# 所以.:nth-child(2)表示当前标签是它的父节点的第二个子节点
product_link_css = "div.protect_con > div:nth-child(2) > div.shop_01-imgbox > a"
# 通过xpath定位元素
iphone = driver.find_element_by_css_selector(product_link_css)
# 删除元素的target属性
driver.execute_script("arguments[0].removeAttribute('target')", iphone)
iphone.click()
# 在商品详情界面,点击加入购物车
driver.find_element_by_id("joinCarButton").click()
# driver.find_element_by_class_name("shopCar_T_span3").click()
driver.find_element_by_css_selector(".shopCar_T_span3").click()
# 点击结算按钮
# 在每个class前面都加一个小数点,并且去掉中间的空格, 我们就可以同时用两个属性定位一个元素
driver.find_element_by_css_selector(".shopCar_btn_03.fl").click()
# 点击添加新地址
driver.find_element_by_css_selector(".add-address").click()
# 输入收货人等信息(选择地区下午讲)
driver.find_element_by_name("address[address_name]").send_keys("张三")
driver.find_element_by_name("address[mobile]").send_keys("13123412345")
dropdown1 = driver.find_element_by_id("add-new-area-select")
# 下拉框是一种特殊的网页元素, 对下拉框的操作和普通网页元素不太一样
# Selenium为这种特殊的元素,专门创建了一个类Select
# dropdown1的类型是一个普通的网页元素, 下面这句代码的意思是,
# 把一个普通的网页元素,转换成一个下拉框的特殊网页元素
print(type(dropdown1)) # dropdown是WebElement类型
# WebElement这个类中,只有click和send_keys这样的方法,没有选择下拉框选项的方法
select1 =  Select(dropdown1)
print(type(select1)) # select1是Select类型
# 转换成select类型之后,网页元素还是那个元素,但是Select类中有选择选项的方法
select1.select_by_value("320000")     #这时,我们就可以通过选项的值来定位
time.sleep(2)
select1.select_by_visible_text("辽宁省")   #也可通过选项的文本信息来定位
# 尝试一下,选择沈阳市
# 因为是动态id,所以不能通过id定位
# 因为class重复,所以我们也不能直接用class定位
# 但是我们可以用find_elements的方法,先找到页面中所有class=add-new-area-select的元素,
# 然后在通过下标的方式选择第n个页面元素,
# 这种方法类似于以前学的javascript方法
dropdown2 = driver.find_elements_by_class_name("add-new-area-select")[1]
Select(dropdown2).select_by_visible_text("沈阳市")
# 自己选一个铁西区
# driver.find_elements_by_class_name("add-new-area-select")[2]等同于下面这句
# tag_name()这个方法,大多数情况都能找到一堆元素,
# 所以  find_element_tag_name()这个方法很少用
# 但是  find_elements_tag_name()[n]这个方法比较常用
dropdown3 = driver.find_elements_by_tag_name("select")[2]
Select(dropdown3).select_by_visible_text("铁西区")
# 点击点击,保存收获人信息
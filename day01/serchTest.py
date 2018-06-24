# 1.打开主页
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://172.31.15.27:8081/")
# 2.点击登录
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[2]/a[1]").click()
# 3.搜索框输入iPhone
# driver.find_element_by_name("keyword").send_keys("iphone")
# 如果我们想在新的标签页上操作页面元素,怎么办?
# 需要进行窗口切换
# driver.switch_to_window(第二个窗口的名字)
# 接下来的问题是,如何获取第二个窗口的名字
# selenium提供了浏览器所有窗口的名字集合
# handles 是句柄的意思,把句柄理解为名字就可以了
# driver.window_handles 可以理解为是一个数组,我要取第二个窗口的名字
# [1]表示数组的第二个元素
#所以,第二个窗口的名字是 driver.window_handles[1]
# 所以窗口切换的语句就是
driver.switch_to.window(driver.window_handles[1])

driver.find_element_by_name("keyword").send_keys("iphone")
# [1]表示第二个元素,[-1]表示最后一个元素
# 在python中元组和列表可以正着从0开始数,
# 也可以负着从-1开始数,倒数第一个-1,倒数第二个-2
# 所以上面的代码可以改成以下方式
# driver.switch_to.window(driver.window_handles[-1])
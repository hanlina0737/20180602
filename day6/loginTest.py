
from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver
# from selenium.webdriver.support import expected_conditions
# as EC把expected_conditions名字缩写成简单的
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("http://localhost/index.php?m=user&c=public&a=login")
driver.find_element_by_name("username").send_keys("fanxiao")
driver.find_element_by_id("password").send_keys("111111")
driver.find_element_by_class_name("login_btn").click()
# 因为中间存在一个登录成功页面,所以不能直接点击该链接
# 解决办法三种方式 固定等待time.sleep 隐式等待 现实等待
# WebDriverWait(driver,20,0.5).until(expected_conditions)
WebDriverWait(driver,20,0.5).until(EC.visibility_of_element_located((By.LINK_TEXT,"进入商城购物")))
# 这个是显示等待的代码,相当于time.sleep(20)
driver.find_element_by_link_text("进入商城购物").click()


from selenium.webdriver.common.by import By


class MemberCenterPage:
    def __init__(self,driver):
        # self.driver = webddriver.Chrom()
        self.driver = driver
        self.url = "http://localhost/index.php?m=user&c=public&a=login"


    welcome_link_loc = (By.PARTIAL_LINK_TEXT,"您好")
    # get_welcom_link_text()用于返回"您好,fanxiao"

    def get_welcome_link_text(self):
        return self.driver.find_element(*self.welcome_link_loc).text
    # 如果当前类中,赋值driver时没有先用driver = webdriver.Chrom(),那么后面写代码想用selenium方法时因为IDE不知道driver的类型就没有办法给出提示信息
    # 比如在输入self.driver时,后面不会自动提示find_element这个方法
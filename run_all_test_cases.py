#这个文件时用来批量执行unittest的测试用例
# 该文件是我们这个测试工具的唯一入口
# 1.导入unittest,因为批量执行测试用例的功能由unittest代码库提供
import smtplib
import unittest

import os
from email.mime.text import MIMEText

from package.HTMLTestRunner import HTMLTestRunner
def send_mail(path):
#    1. 通过path打开测试报告文件
# html格式不是文本格式需要指定打开方式是二进制
    file=open(path,'rb')
# 2.读取文件的内容作为邮件正文
    msg = file.read()
# 3.把读取出来的内容转换成MIMEText格式
# 电子邮件的类型一般有三种,分别是 纯文本plain,html,富文本
    mime = MIMEText(msg, _subtype='html', _charset='utf-8')
# 4.除了正文以外,还需要设置主题,发件人,收件人
    mime['subject']='博为峰自动化测试报告'
    # 因为发件人需要登录密码,这里的密码不是真正的密码,是客户端授权码
    mime['from']='bwftest126@126.com'
    # 收件人的邮箱
    mime['to']='fanxiaoqian@126.com'
# 发送邮件
# 1.实现smtp()构造方法
    smtp = smtplib.SMTP()
# 2.链接126邮箱
    smtp.connect("smtp.126.com")
# 3.登录126邮箱
    smtp.login('bwftest126@126.com','abc123asd654')
# 4.发送
    smtp.send_message(mime, from_addr='bwftest126@126.com', to_addrs='fanxiaoqian@126.com')
# 5.退出
    smtp.quit()



if __name__ == '__main__':
    # 2.要想批量执行,首先要明确要执行哪些测试用例
# 只能执行继承了unittest.TestCase的类
# 比如执行这个项目中所有的unittest的测试用例,
#     defaultTestLoader是默认的测试用例的加载器,可以用来发现所有的测试用例
#     类中声明方法必须有self 但是调用方法没有self
#     *表示通配符,可以代替任何字符
#     *Test.py表示以Test.py结尾的所有文件
#     .表示当前路径,即项目的根路径
#     我要想执行第四天和第五天的怎么来写?
#     suite 随便起的变量名,suite本身是测试用例集的意思
    suite = unittest.defaultTestLoader.discover("./day5", pattern='*Test.py')
    # 执行所有的测试用例
    # suite = unittest.defaultTestLoader.discover(".", pattern='*.py')
    # 3.找到测试用例后,执行这些测试用例
    # TextTestRunner()文本的测试用例的运行器
    # unittest.TextTestRunner().run(suite)
    # 4.生成测试报告:首先考虑测试报告的格式应该设计成的样子
#     需要导入一个测试报告的模板 htmlTestRunner(htmlTestRunner也是一个代码库,只是这个代码库中只有一个文件)
# 在项目中创建一个文件夹package
# 把HTMLTestRunner.py赋值到创建的package中
# 4.通过HTMLTestRunner执行所有的测试用例
# HTMLTestRunner类似TextTestRunner()都是批量执行测试用例的,区别在于执行测试用例的输出结果,一个是html网页一个是文本text结果
# Text会被打印到控制台中 html会单独生成一个文件
# 相比于text  html结构更清晰
# 所以二者选其一用htmlTestTunner代替unittest原生的测试用例运行器TexTestRunner
#     我们需要把生成的测试报告保存到一个固定位置方便查看
#     在项目根节点下创建一个文件夹叫report
#   5.  定义测试报告的保存目录
    base_path = os.path.dirname(__file__)
    path = base_path + '/report/test_report.html'
    # 6. 创建测试文件
    file = open(path, 'wb')
    HTMLTestRunner(stream=file, verbosity=1, title="博为峰测试报告", description="测试环境: Server 2008; 浏览器:'Chrome'").run(suite)
    # 7.把测试报告作为邮件发送,好处是,可以起到及时提醒的作用
    # 前提条件,准备两个邮箱
    # 版本控制的前提条件,申请一个git账号
    # 把html格式的测试报告,作为邮件正文发送
    send_mail(path)
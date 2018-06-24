#第一个单元测试框架的示例
#1.要想用unittest框架,首先要导包
# 为什么selenium需要 先安装或者解压?unittest不需要?\
# 因为unittest比selenium更常用,几乎所有测试都要用unittest组织测试
# 所有python把unittest集成在python SDK中了,不需要单独下载,只要安装python就有unittest是python内置的代码库

import unittest
# 2.创建一个类,用来写自动化测试用例
# 这个类需要继承unittest框架中的testcase类
# 我们继承了TestCase这个类,就说明我们这个类是一个测试用例类
# python中的类名最好和文件名不一样,文件名首字母小写,类名首字母大写
# 类名和文件名写法不强制要求格式,只是一个python的习惯
# ()表示继承,java的关键字extends  继承的意思是指子类完全继承父类的所有方法和属性,并且有自己的扩展内容.
class FirstUnitTest(unittest.TestCase):
#     重写父类的setUp 和tearDown方法
#  setUp()方法是在测试用例方法执行之前要做的操作,类似于手工测试用例前置条件
# setup和teardown方法在每个测试用例执行前都会执行一次
    def setUp(self):
        print(1)

    def tearDown(self):
#          tearDown()是在测试用例执行后要做的操作
#           比如可能需要还原测试场景或清除脏数据
        print(2)

    def test_login(self):
#         这个方法用来编写测试步骤
# 框架规定测试用例方法必须以test开头
# 只有以test开头的方法才能被当做测试用例被执行,,如下面的窗口切换我不想让他执行只想被调用
        print(3)
    def switch_window(self):
#         窗口切换方法只是希望被调用才能执行
        print(4)

    def test_zhuce(self):
        # 在python中类里面的每一个方法都有一个默认参数叫self
        # self类似与java中的this关键字代表类本身
        # 如果想使用类的属性和方法那么必须在前面加self关键字
        # 根据光标的所在的位置来决定执行什么测试用例
        # 光标在哪个方法中那么就会只运行哪个测试用例
        # 光标在unittest..main这行就会执行所有的测试用例
        # 测试用例一个类中所有测试用例方法的执行顺讯是根据方法名的字母顺序决定的
        self.switch_window()
#     也可以选择重写setUpClass和tearDownClass方法
    @classmethod
    # @classmethod在python中叫装饰器在java中叫注解
    def setUpClass(cls):
        print(5)
    @classmethod
    def tearDownClass(cls):
        print(6)
#     写完后全部运行一下检查setupclass和setup有什么不同
# classmethod只在类中所有方法前或者所有方法后执行一次

#     if __name__ == '__main__':这是一个固定的写法
# 就是在程序运行时,通过这句话可以自动判断是不是在当前文件开始执行的
# 在程序运行时,通过这句话,可以自动判断当前文件是不是程序入口
# 如果当前文件是程序的入口,那么就会执行if子句中的内容
if __name__ == '__main__':
    # 可以理解为当前文件的主函数,会自动调用类中的方法
    # 所以if __name__ == '__main__':的意思是
    # __name__指的是当前文件
    # ++main__指的是程序入口
    # if __name__ == '__main__':类似于main函数,只能它调用别人,别人不能调用它
    unittest.main()

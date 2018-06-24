#1.导包
import csv

import os
# [1,2,3]这种是一维列表,,[1,2,3][1,2,3],[1,2,3]这就是二维列表,列表中的一个元素也是也是一个列表就是二维列表
class CsvFileManager4:
    # def read(self):
    def read(self,filename):
        list= []#声明一个空列表
    #     2.指定csv文件的路径
        path =r"C:\Users\51Testing\PycharmProjects\20180602\data\test_data.csv"
#     这样生成的path路径有一个缺点,可移植性比较差
# 在公司中,一个项目往往是多人写作完成的
#有的人可能把项目放在自己的c盘,有的人放在d盘
#项目换了不同l路径,那么我们每次都不得不修改代码
#更好的方法是
        # os.path.dirname(__file__)是一个固定写法,用来获取当前文件的目录结构
        # os操作系统,path路径,dirname目录名,__file__shipython内置的变量,表示当前文件
        #
        base_path = os.path.dirname(__file__)
        print(base_path)
# 用base_path的好处,不管项目放在任何路径下面,都可以找到该文件的绝对路径
# 我们真正想要的是csv文件的路径不是代码的路径,二者的区别在哪
# 所以可以通过base_path计算出csv路径
        path = base_path.replace('day5','data/test_data.csv')
        print(path)
#         打开指定文件
        file = open(path,'r')
#         每次打开文件最后用完要关闭该文件,释放系统资源
# 我们上节课用的是try...finally
# 更常用的方法是with..as的预防结构
        with open(path,'r') as file:
            data_table = csv.reader(file)
            # 4.循环遍历数据表中的每一行
            for row in data_table:
                print(row)
#        打印出来不是我们的目的,我们的测试用例需要调用这些数据
#所以要给这个方法设一个返回值,把数据提取出来
#             声明一个二维列表,保存data_table中的所有数据
                list.append(row)
#         6.在read方法的末尾,返回这个列表
        return list
#     7.这个方法写完之后,是不是所有的测试用例都应该从这个方法读取csv数据
# 我们不可能为每个测试用例都单独写这么一个方法
# 但是现在这个路径已经写死了,只能读test_data.csv这个文件
# 一个csv文件只适合保存一组测试用例的数据,
# 所以不同的测试用例应该对应不同的csv文件
# 7.把csv文件名作为参数传进来def read(self):--->def read(self,filename):

if __name__ == '__main__':
   list = CsvFileManager4().read('test_data.csv')
   print(list[1][0])
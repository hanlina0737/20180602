#1.要想读取csv文件,首先要导入csv代码库
# 这个csv也不要下载,因为它很常用python内置的代码库,如果要读取excel需要下载相应的代码库:xlrd--可以通过命令下载,dos窗口中输入pip install -U xlrd
# 也可以通过命令行在线安装,老师发的selenium的离线包,  pip install -U selenium或者pip3 nstall selenium
# -U可以省略 是升级到最新版的意思
# pip是python语言最常用的项目管理工具和java中maven类似
# 如果装了python2同时安装了python3 要用pip3 install -U xlrd
# 或者点击file--settings--project下的interpreter--+
# 搜索需要的代码哭并可直接安装
import csv
# 2.指定要读取的文件的路径
# path = 'C:\Users\51Testing\PycharmProjects\20180602\data\test_data.csv'
# print(path)
# 运行会报错,因为字符串中包含反斜线\会当做转义字符,怎么办呢?
# 1.每个反斜线前面加一个反斜线;2.把每个反斜线改成正斜线/;3.相比第二章方法更好一点,因为java  python都是跨平台语言,
# 在字符串中,两个反斜线会自动转成一个反斜线
# 在windows操作系统中,用反斜线表示目录解雇,但是在linux操作系统中,只有正斜线才能表示目录,如果用双反斜线,那么代码就是去了跨平台的能力,用不了反斜线
# 如果用正斜线,代码可以同时在linux和windows中执行
# 在字符串外面加上一个字母r,认为中间所有的代码都不存在转义字符
path = r'C:\Users\51Testing\PycharmProjects\20180602\data\test_data.csv'
print(path)
# 3.打开路径所对应的文件
file = open(path,'r')
# 4.读取文件的内容,通过csv代码库,
# reader()方法是专门用来读取文件的
data_table = csv.reader(file)
# 5.打印data_table中的每一行数据,循环for-each
# for是循环的关键字,item代表每一行,每循环一次item代表最新的一行数据
# data_table 表示整个文件中的所有数据
for item in data_table:
    print(item)
    # 我们是不是这样就成功从excel中读取了所有数据
    # 很多的测试用例可能都需要从excel中读取数据,所以我们应该对这些代码做一个简单的封装,建一个文件叫csvFileManager2,把以上代码封装到一个方法中并且在建一个文件去读取封装的方法
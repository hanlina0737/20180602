import csv
# 每个测试用例对应着不同的csv文件
# 每条测试用例都会打开一个csv文件,所以每次页应该关闭该文件
# 把读取文件的代码封装成一个方法
class CsvFileManager3:
    @classmethod
    def read(self):
        path = r'C:\Users\51Testing\PycharmProjects\20180602\data\test_data.csv'
        file = open(path,'r')
        try:       #尝试执行以下代码
            data_table = csv.reader(file)
            #a = [2,3,4,5,6]
           # a[6]# 这时可能发生数组下标越界
            # 如何保证不论程序执行过程中是否报错,都能正常关闭打开的文件
            # 加上try finally
            for item in data_table:
                print(item)
        finally:   #finally最终,不论程序是不是报错都会执行以下代码
            #     关闭文件
            file.close()

            print("file.close() method is executed")
if __name__ == '__main__':
    # 如果在方法上面加上classmethod表示这个方法可以直接用类调用, 就不需要先实例化对象后才能调用了
    CsvFileManager3.read()
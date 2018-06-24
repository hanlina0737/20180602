import csv
# 把读取文件的代码封装成一个方法
class CsvFileManager2:
    def read(self):
        path = r'C:\Users\51Testing\PycharmProjects\20180602\data\test_data.csv'
        file = open(path,'r')
        data_table = csv.reader(file)

        for item in data_table:
            print(item)
if __name__ == '__main__':
    # 实例化对象
    csvr = CsvFileManager2()
    csvr.read()
    # 如果在方法上面加上classmethod表示这个方法可以直接用类调用,就不需要先实例化对象后才能调用了
    # 直接写CsvFileManager2.read()
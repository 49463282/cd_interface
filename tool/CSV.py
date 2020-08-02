# coding=utf-8
import csv


class CSV:

    def assertResult(self, except_value, real_value):
        '''
        校验样本字符串中是否包含指定字符串
        :param except_value: string 指定字符串
        :param real_value: string 样本字符串
        :return: Boolean 样本中包含指定字符串返回True,否则返回False
        '''
        ifsuccess = except_value in str(real_value)
        return ifsuccess

    def writeCSV(self, filename, results, headers):
        '''
        写入csv文件指定内容
        :param filename: string 需要写入的文件名称
        :param results: [{data1},{data2},...] 写入的内容
        :return: 无
        '''
        # 以DictWriter的方式写文件
        with open(filename, 'w+') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            # 写表头
            writer.writeheader()
            # 写数据
            if results.__len__() > 0:
                for result in results:
                    writer.writerow(result)
            csvfile.close()

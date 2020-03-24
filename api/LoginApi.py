# coding=utf-8
import requests
import app
import csv
import json
import time
import unittest

class Login:
    def __init__(self):
        self.data_file = "C:\\Users\\hp\\PycharmProjects\\cd_interface\\data\\login_test.csv"

    def readCSV(self, filename):
        '''
        :param filename: 需要读取的数据文件
        :return: [{data1},{data2}...]
        '''
        try:
            datas = []
            # 以DictReader的方式读取数据文件，方便与json互做转换
            with open(filename, 'r') as csvfile:
                # 从文件里读取到的数据转换成字典列表的格式
                reader = csv.DictReader(csvfile)
                for row in reader:
                    data = {}
                    data['id'] = row['id']
                    data['tenantId'] = row['tenantId']
                    data['mobile'] = row['mobile']
                    data['password'] = str(row['password'])
                    data['uuid'] = str(row['uuid'])
                    data['brandType'] = row['brandType']
                    data['type'] = row['type']
                    data['expect'] = json.dumps(row['expect']) \
                        if isinstance(row['expect'], dict) \
                        else row['expect']
                    datas.append(data)
                return datas
        except FileNotFoundError:
            return datas

    def assertResult(self, except_value, real_value):
        '''
        校验样本字符串中是否包含指定字符串
        :param except_value: string 指定字符串
        :param real_value: string 样本字符串
        :return: Boolean 样本中包含指定字符串返回True,否则返回False
        '''
        ifsuccess = except_value in str(real_value)
        return ifsuccess

    def writeCSV(self, filename, results):
        '''
        写入csv文件指定内容
        :param filename: string 需要写入的文件名称
        :param results: [{data1},{data2},...] 写入的内容
        :return: 无
        '''
        # 以DictWriter的方式写文件
        with open(filename, 'w+') as csvfile:
            headers = "id,tenantId,mobile,password,uuid,code,brandType,type,expect,real_value,assert_value".split(
                ",")
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            # 写表头
            writer.writeheader()
            # 写数据
            if results.__len__() > 0:
                for result in results:
                    writer.writerow(result)
            csvfile.close()

    # def get_login(self,params, heda):
    #     # data_file = "..\data\login_test.csv"
    #     response = requests.post(self, json.dumps(params), headers=heda)
    #     return response
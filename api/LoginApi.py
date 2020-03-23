# coding=utf-8
import requests
import app
import csv
import json
import time


class Login:
    def __init__(self):
        self.url = app.BASE_URL + '/manager/sysuser/login'
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
                    print(datas)
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
            headers = "tenantId,mobile,password,uuid,code,brandType,type,expect,real_value,assert_value".split(
                ",")
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            # 写表头
            writer.writeheader()
            # 写数据
            if results.__len__() > 0:
                for result in results:
                    writer.writerow(result)
                    csvfile.close()

    def get_login(self, code):
        # data_file = "..\data\login_test.csv"
        data_file = "C:\\Users\\hp\\PycharmProjects\\cd_interface\\data\\login_test.csv"
        # 指定最终结果生成的数据文件名称
        result_file = "C:\\Users\\hp\\PycharmProjects\\cd_interface\\report\\result_{}.csv".format(
            str(time.time()).split(".")[0])
        data = self.readCSV(data_file)
        # 数据文件有内容则调用接口，否则直接测试结束
        if data.__len__() > 0:
            results = []
            for testcase in data:
                result = {}
                result["tenantId"] = testcase["tenantId"]
                result["mobile"] = testcase["mobile"]
                result["password"] = testcase["password"]
                result["code"] = code
                result["uuid"] = testcase["uuid"]
                result["brandType"] = testcase["brandType"]
                result["type"] = testcase["type"]
                result["expect"] = testcase["expect"]
                # 组装参数
                params = {
                    "tenantId": result["tenantId"],
                    "mobile": result["mobile"],
                    "password": result["password"],
                    "code": result["code"],
                    "uuid": result["uuid"],
                    "brandType": result["brandType"],
                    "type": result["type"]
                }
                # data = {"tenantId": 100, "mobile": "18549811213", "password": "qwe123", "code": code,
                #         "uuid": "1e4cfdb3-ba66-4082-892b-13ba4059436d", "brandType": 1, "type": 0}
                print(params)
                heda = {
                    "token": app.TOKEN,
                    "Content-Type": "application/json;charset=UTF-8"
                }
                response = requests.post(self.url, json.dumps(params), headers=heda)

                # 调用assert方法，检查预期结果是否在响应结果中存在
                assert_value = self.assertResult(result["expect"], response.json().get("message"))
                result["real_value"] = response.text
                result["assert_value"] = assert_value
                # 获取每一行里的所有字段以及实际结果和验证结果
                results.append(result)
                # 执行完所有记录后，将所有结果写入result.csv
                self.writeCSV(result_file, results)  # 写入csv文件
                return response

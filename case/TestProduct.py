# coding=utf-8
import unittest

import requests
from tools.PyMysql_cd import DBUtil
import app
from tools.Request import Request
import time
import json
import csv


class TestProduct(unittest.TestCase):

    # 初始化与销毁
    def setUp(self):
        self.hade = {
            "token": app.TOKEN,
            "Content-Type": "application/json;charset=UTF-8"
        }

    def test_product_add(self):
        data = {"name": "接口测试", "categoryList": [], "labelList": [], "materialMainList": [{"id": 12638, "rank": 1}],
                "materialnotMainList": [], "details": "接口测试", "showImages": "", "productCode": "", "weight": "0",
                "volume": "0", "virtualTotal": "", "type": 1, "status": 0, "isOpen": 1,
                "commissionRulesDTO": {"empAmount": "1", "empPercent": "", "empType": 2, "empSwitch": 1, "id": ""},
                "expressFree": 1, "attributeList": [{"key": "颜色",
                                                     "value": [{"values": "红色", "img": ""}, {"values": "绿色", "img": ""},
                                                               {"values": "黄色", "img": ""}], "isShow": 1}, {"key": "尺寸",
                                                                                                            "value": [{
                                                                                                                "values": "150cm",
                                                                                                                "img": ""},
                                                                                                                {
                                                                                                                    "values": "160cm",
                                                                                                                    "img": ""}],
                                                                                                            "isShow": 1}],
                "specificationList": [
                    {"id": "", "imgUrl": "", "inventory": "99", "prePrice": "199", "price": "99", "specCode": "",
                     "specContent": "红色，150cm", "status": 1},
                    {"id": "", "imgUrl": "", "inventory": "99", "prePrice": "199", "price": "99", "specCode": "",
                     "specContent": "红色，160cm", "status": 1},
                    {"id": "", "imgUrl": "", "inventory": "99", "prePrice": "199", "price": "99", "specCode": "",
                     "specContent": "绿色，150cm", "status": 1},
                    {"id": "", "imgUrl": "", "inventory": "99", "prePrice": "199", "price": "99", "specCode": "",
                     "specContent": "绿色，160cm", "status": 1},
                    {"id": "", "imgUrl": "", "inventory": "99", "prePrice": "199", "price": "99", "specCode": "",
                     "specContent": "黄色，150cm", "status": 1},
                    {"id": "", "imgUrl": "", "inventory": "99", "prePrice": "199", "price": "99", "specCode": "",
                     "specContent": "黄色，160cm", "status": 1}],
                "batch": {"prePrice": "199", "price": "99", "inventory": "99"}, "isVip": 1}
        url = app.BASE_URL + "/manager/product/add"
        response = requests.post(url, json.dumps(data), headers=self.hade)
        self.assertEqual("成功", response.json().get("message"))

    def test_product_delete(self):
        database = "cd-product_uat"
        conn = DBUtil.get_connect(database)
        cursor = DBUtil.get_cursor(conn)
        sql = 'select id from t_product where name = "接口测试" and tenant_id = 100 and `status` = 0 order by create_time desc limit 1'
        cursor.execute(sql)
        r = cursor.fetchone()
        id = str(r[0])
        DBUtil.close_res(cursor, conn)
        response = requests.get(app.BASE_URL + "/manager/product/delete?productId=" + id, self.hade)
        self.assertEqual("成功", response.json().get("message"))

    # def readCSV(self, filename):
    #     '''
    #     :param filename: 需要读取的数据文件
    #     :return: [{data1},{data2}...]
    #     '''
    #     try:
    #         datas = []
    #         # 以DictReader的方式读取数据文件，方便与json互做转换
    #         with open(filename, 'r') as csvfile:
    #             # 从文件里读取到的数据转换成字典列表的格式
    #             reader = csv.DictReader(csvfile)
    #             for row in reader:
    #                 data = {}
    #                 data['id'] = row['id']
    #                 data['method'] = row['method']
    #                 data['tenantId'] = row['tenantId']
    #                 data['mobile'] = row['mobile']
    #                 data['password'] = str(row['password'])
    #                 data['uuid'] = str(row['uuid'])
    #                 data['brandType'] = row['brandType']
    #                 data['type'] = row['type']
    #                 data['expect'] = json.dumps(row['expect']) \
    #                     if isinstance(row['expect'], dict) \
    #                     else row['expect']
    #                 datas.append(data)
    #             return datas
    #     except FileNotFoundError:
    #         return datas
    #
    # def assertResult(self, except_value, real_value):
    #     '''
    #     校验样本字符串中是否包含指定字符串
    #     :param except_value: string 指定字符串
    #     :param real_value: string 样本字符串
    #     :return: Boolean 样本中包含指定字符串返回True,否则返回False
    #     '''
    #     ifsuccess = except_value in str(real_value)
    #     return ifsuccess
    #
    # def writeCSV(self, filename, results, headers):
    #     '''
    #     写入csv文件指定内容
    #     :param filename: string 需要写入的文件名称
    #     :param results: [{data1},{data2},...] 写入的内容
    #     :return: 无
    #     '''
    #     # 以DictWriter的方式写文件
    #     with open(filename, 'w+') as csvfile:
    #         writer = csv.DictWriter(csvfile, fieldnames=headers)
    #         # 写表头
    #         writer.writeheader()
    #         # 写数据
    #         if results.__len__() > 0:
    #             for result in results:
    #                 writer.writerow(result)
    #         csvfile.close()
    #
    # def test_login(self):
    #     data_file = "C:\\Users\\hp\\PycharmProjects\\cd_interface\\data\\login_test.csv"
    #     # 指定最终结果生成的数据文件名称
    #
    #     data = self.readCSV(data_file)
    #     # 数据文件有内容则调用接口，否则直接测试结束
    #     if data.__len__() > 0:
    #         results = []
    #         result_file = "C:\\Users\\hp\\PycharmProjects\\cd_interface\\report\\result_{}.csv".format(
    #             str(time.time()).split(".")[0])
    #         for testcase in data:
    #             result = {}
    #             result["id"] = testcase["id"]
    #             result["method"] = testcase["method"]
    #             result["tenantId"] = testcase["tenantId"]
    #             result["mobile"] = testcase["mobile"]
    #             result["password"] = testcase["password"]
    #             result["code"] = self.code
    #             result["uuid"] = testcase["uuid"]
    #             result["brandType"] = testcase["brandType"]
    #             result["type"] = testcase["type"]
    #             result["expect"] = testcase["expect"]
    #             # 组装参数
    #             params = {
    #                 "tenantId": result["tenantId"],
    #                 "mobile": result["mobile"],
    #                 "password": result["password"],
    #                 "code": result["code"],
    #                 "uuid": result["uuid"],
    #                 "brandType": result["brandType"],
    #                 "type": result["type"]
    #             }
    #             # response = Login.get_login(url, params, heda)
    #             response = Request().httprequest(result["method"], self.url, params, self.hade)
    #             # 调用assert方法，检查预期结果是否在响应结果中存在
    #             assert_value = self.assertResult(result["expect"], response.json().get("message"))
    #             result["real_value"] = response.text
    #             result["assert_value"] = assert_value
    #             # 获取每一行里的所有字段以及实际结果和验证结果
    #             results.append(result)
    #             # 执行完所有记录后，将所有结果写入result.csv
    #             self.writeCSV(result_file, results)  # 写入csv文件

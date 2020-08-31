# coding=utf-8
import unittest
import requests
import app
from tools.CSV import CSV
from tools.Request import Request
from tools.Redis import DBRedis
import time
import json
import csv
import os
from tools.Logging import Log


class ApiLogin(unittest.TestCase):
    # 初始化与销毁
    # def setUp(self):
    #     #   请求头
    #     self.
    log = Log()

    def api_login(self):
        # 调用请求业务
        requests.get(app.BASE_URL + "/manager/sysuser/imagecode?uuid=038add55-52dd-4e22-b2a7-78306d3b0074")
        r = DBRedis.get_connect()
        # 查询图形验证码
        code = r.get('image:code:uuid:038add55-52dd-4e22-b2a7-78306d3b0074')
        url = app.BASE_URL + '/manager/sysuser/login'
        data = {"tenantId": 100, "mobile": "18549811212", "password": "qwe123", "code": code,
                "uuid": "038add55-52dd-4e22-b2a7-78306d3b0074", "brandType": 1, "type": 0}
        self.log.info(u"获取登录图形验证码：%s" % code)
        self.log.info(u"请求登录URL：%s" % url)
        self.log.info(u"请求参数 ：%s" % data)
        response = requests.post(url, data=json.dumps(data), headers=app.headers)
        token = response.json().get("data").get("token")
        # app.TOKEN = token
        app.headers["token"] = token
        # 返回请求结果
        return response

    # def api_login(self):
    #     # 获取测试用例的路径
    #     data_file = os.path.abspath("data") + "\\login_test.csv"
    #     # 指定最终结果生成的数据文件名称
    #     result_file = os.path.abspath("report") + "\\login_{}.csv".format(str(time.time()).split(".")[0])
    #     # 打开测试用例
    #     data = self.readCSV(data_file)
    #     # 数据文件有内容则调用接口，否则直接测试结束
    #     if data.__len__() > 0:
    #         results = []
    #         for testcase in data:
    #             # 生成图形验证码
    #             requests.get(app.BASE_URL + "/manager/sysuser/imagecode?uuid=038add55-52dd-4e22-b2a7-78306d3b0074")
    #             r = DBRedis.get_connect()
    #             # 查询图形验证码
    #             code = r.get('image:code:uuid:038add55-52dd-4e22-b2a7-78306d3b0074')
    #             result = {}
    #             result["id"] = testcase["id"]
    #             result["method"] = testcase["method"]
    #             result["tenantId"] = testcase["tenantId"]
    #             result["mobile"] = testcase["mobile"]
    #             result["password"] = testcase["password"]
    #             result["code"] = code
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
    #             response = Request().httprequest(result["method"], self.url, params, self.hade)
    #             # 调用assert方法，检查预期结果是否在响应结果中存在
    #             assert_value = CSV().assertResult(result["expect"], response.json().get("message"))
    #             result["real_value"] = response.text
    #             result["assert_value"] = assert_value
    #             # 获取每一行里的所有字段以及实际结果和验证结果
    #             results.append(result)
    #             # 执行完所有记录后，将所有结果写入result.csv
    #             headers = "id,method,tenantId,mobile,password,uuid,code,brandType,type,expect,real_value,assert_value".split(
    #                 ",")
    #             CSV().writeCSV(result_file, results, headers)  # 写入csv文件

# class base:
#     host_name = {
#         "pre": "",
#         "prod": "",
#     }
#
#     def __init__(self, token):
#         self.token = token
#
#     def request(self, api_name, params=None, data=None, headers=None, method="GET"):
#         method = method.upper()
#         url = f"{self.host_name}{api_name}"
#         # token = ""
#         params = {
#
#         }
#         if "token" not in headers:
#             headers["token"] = self.token
#
#         response = requests.request(method, params=params, json=data, headers=headers)
#         if response.status_code == 200:
#             return self.response_data(response.json())
#         else:
#             raise ValueError("status code wrong.")
#
#     def response_data(self, data):
#         # data["timestamp"] = time.mkt
#         return data
#
#
# class product(base):
#     def __init__(self, token):
#         super.__init__(token)
#
#     def create(self, data):
#         api_name = "/manger/product/add"
#         resposne = self.request(api_name, data=data, method="post")
#         return resposne
#
#     def create_demo(self):
#         data = {
#             "id": 0,
#             "product_name": "",
#         }
#         return self.create(data)
#
#     def update(self, _id, data):
#         pass
#
#
# p = product()

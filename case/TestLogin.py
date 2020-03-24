# coding=utf-8
import unittest
from api.LoginApi import Login
import requests
import app
from tools.Request import Request
from tools.redis_uat import DBRedis
import time
import json


class TestLogin(unittest.TestCase):

    # 初始化与销毁
    def setUp(self):
        self.Login = Login()
        requests.get(app.BASE_URL + "/manager/sysuser/imagecode?uuid=1e4cfdb3-ba66-4082-892b-13ba4059436d")

    def test_login(self):
        # 查询图形验证码
        r = DBRedis.get_connect()
        code = r.get('image:code:uuid:1e4cfdb3-ba66-4082-892b-13ba4059436d')
        # 调用请求业务
        data_file = "C:\\Users\\hp\\PycharmProjects\\cd_interface\\data\\login_test.csv"
        # 指定最终结果生成的数据文件名称

        data = self.Login.readCSV(data_file)
        # 数据文件有内容则调用接口，否则直接测试结束
        if data.__len__() > 0:
            results = []
            result_file = "C:\\Users\\hp\\PycharmProjects\\cd_interface\\report\\result_{}.csv".format(
                str(time.time()).split(".")[0])
            for testcase in data:
                result = {}
                result["id"] = testcase["id"]
                result["method"] = testcase["method"]
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
                heda = {
                    "token": app.TOKEN,
                    "Content-Type": "application/json;charset=UTF-8"
                }
                url = app.BASE_URL + '/manager/sysuser/login'
                # response = Login.get_login(url, params, heda)
                response = Request().httprequest(result["method"], url, params, heda)
                # 调用assert方法，检查预期结果是否在响应结果中存在
                assert_value = self.Login.assertResult(result["expect"], response.json().get("message"))
                result["real_value"] = response.text
                result["assert_value"] = assert_value
                # 获取每一行里的所有字段以及实际结果和验证结果
                results.append(result)
                # 执行完所有记录后，将所有结果写入result.csv
                self.Login.writeCSV(result_file, results)  # 写入csv文件
                # token = response.json().get("data").get("token")
                # app.TOKEN = token
                # 断言判断
                # self.assertEqual(200, response.json().get("status"))

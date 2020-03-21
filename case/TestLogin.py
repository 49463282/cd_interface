# coding=utf-8
import unittest
from api.LoginApi import Login
import requests
import app
from api.redis_uat import DBRedis


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
        response = self.Login.get_login(code)
        token = response.json().get("data").get("token")
        app.TOKEN = token
        # 断言判断
        self.assertEqual(200, response.json().get("status"))

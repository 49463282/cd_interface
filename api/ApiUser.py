# coding=utf-8
import os
import unittest
import requests
from tools.PyMysql_cd import DBUtil
import app_tool
from tools.Request import Request
import time
import json


class ApiUser(unittest.TestCase):

    # 查询分公司列表
    def api_store_get_sysuser_store_tree(self, headers):
        url = app_tool.BASE_URL + "/manager/store/get_sysuser_store_tree"
        data = {"isFilter": 0}
        response = requests.post(url, json.dumps(data), headers=headers)
        return response

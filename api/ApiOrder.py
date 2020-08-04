# coding=utf-8
import requests
import unittest
import app_tool
from tools.Redis import DBRedis
from tools.PyMysql_cd import DBUtil
import json


class ApiOrder(unittest.TestCase):

    def api_orderreturn_add(self):
        url = app_tool.BASE_URL + "/miniapp/orderreturn/add"
        list = ["D1662020080417420299624"]
        for order_code in list:
            sql = 'select user_id,tenant_id from t_order where order_code = "%s"' % order_code
            database = 'cd-order_uat'
            r = DBUtil.product(sql, database)
            I = DBUtil.fetch(r, 'fetchone')
            userId = int(I[0])
            tenantId = int(I[1])
            # 查询用户token
            ro = DBRedis.get_connect()
            user = ('user:security:userId:%d:%d') % (tenantId, userId)
            token = ro.get(user)
            sql = 'select id,spec_id from t_order_detail where order_code = "%s"' % order_code
            r = DBUtil.product(sql, database)
            re = DBUtil.fetch(r, 'fetchone')
            detailId = str(re[0])
            specId = str(re[1])
            data = {"type": 1, "explain": "", "orderCode": order_code, "specId": specId,
                    "detailId": detailId, "applyNumber": 1, "evidencePic": "", "reason": 2, "v": "2.6.0"}
            print(data)
            headers = {
                "token": token,
                "Content-Type": "application/json;charset=UTF-8"
            }
            response = requests.post(url, json.dumps(data), headers=headers)
            print(response.text)
            assert 200, response.json().get("status")

# coding=utf-8
import json
import unittest

import requests

import app
from tools.PyMysql_cd import DBUtil
from tools.Redis import DBRedis


class TestOrder(unittest.TestCase):
    # 初始化与销毁
    def setUp(self):
        r = DBRedis.get_connect()
        token = r.get("user:security:userId:100:53956")
        self.heda = {"token": token,
                     "Content-Type": "application/json;charset=UTF-8"}

    def test_create_order(self):
        database = "cd-product_uat"
        conn = DBUtil.get_connect(database)
        cursor = DBUtil.get_cursor(conn)
        sql = 'select id from t_store_product where name = "接口测试" and tenant_id = 100 and store_id = 27116'
        cursor.execute(sql)
        r = cursor.fetchone()
        productId = str(r[0])
        sql = 'select * from t_store_specification_19 where product_id = %s' % (productId)
        cursor.execute(sql)
        r = cursor.fetchone()
        specId = str(r[0])
        url = app.BASE_URL + "/miniapp/order/create"
        data = {"orderType": 1, "couponCustomerId": 0, "expressId": "51", "receiverId": 119, "remark": "", "isTake": 0,
                "productList": [{"productId": productId, "specId": specId, "productNum": 1}], "source": 0,
                "v": "2.6.0"}
        response = requests.post(url, json.dumps(data), headers=self.heda)
        self.assertEqual("成功", response.json().get("message"))

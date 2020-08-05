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
        # 查询一个用户的user_id
        database = "cd-user_uat"
        conn = DBUtil.get_connect(database)
        self.cursor = DBUtil.get_cursor(conn)
        sql = "select id from t_user where company_id = %d and type = 0 and status = 1 and tenant_id = 100 order by " \
              "last_login_time desc" % companyId
        self.cursor.execute(sql)
        r = self.cursor.fetchone()
        global userId
        userId = int(r[0])
        r = DBRedis.get_connect()
        token = r.get("user:security:userId:100:%d" % userId)
        self.heda = {"token": token,
                     "Content-Type": "application/json;charset=UTF-8"}

    def test_cart_temporary_add(self):  # 添加临时购物车
        # 查询一个门店id
        sql = 'select id from t_store where parent_id = %d and status = 1' % companyId
        self.cursor.execute(sql)
        r = self.cursor.fetchone()
        storeId = int(r[0])
        database = "cd-product_uat"
        conn = DBUtil.get_connect(database)
        cursor = DBUtil.get_cursor(conn)
        sql = 'select id from t_store_product_%d where name = "%s" and tenant_id = 100 and store_id = %s' % (
            store, product_name, storeId)
        cursor.execute(sql)
        r = cursor.fetchone()
        productId = str(r[0])
        sql = 'select id from t_store_specification_%d where product_id = %s' % (store, productId)
        cursor.execute(sql)
        r = cursor.fetchone()
        specId = str(r[0])
        url = app.BASE_URL + "/miniapp/cart/temporary/add"
        data = {"list": [{"productId": productId, "specId": specId, "number": 1}], "v": "2.6.0"}
        response = requests.post(url, json.dumps(data), headers=self.heda)
        self.assertEqual("处理成功", response.json().get("message"))

    def test_receiveaddress_add(self):  # 添加收获地址
        url = app.BASE_URL + '/miniapp/receiveaddress/add'
        data = {"id": "", "name": "明", "phone": "18449811211", "region": ["北京市", "北京市", "东城区"], "address": "31566165",
                "postcode": "", "isDefault": 0, "province": "北京市", "city": "北京市", "area": "东城区", "v": "2.6.0"}
        response = requests.post(url, json.dumps(data), headers=self.heda)
        self.assertEqual("添加成功", response.json().get("message"))

    def test_create_order(self):  # 创建订单
        # 查询该收货人地址id
        database = 'cd-user_uat'
        conn = DBUtil.get_connect(database)
        cursor = DBUtil.get_cursor(conn)
        sql = 'select id from t_receiver_address where user_id = %d and is_deleted = 0 and tenant_id = 100' % userId
        cursor.execute(sql)
        r = cursor.fetchone()
        receiverId = int(r[0])
        url = app.BASE_URL + "/miniapp/order/create"
        data = {"couponCustomerId": "", "expressId": "", "receiverId": receiverId, "remark": "", "isTake": 0,
                "v": "2.6.0"}
        response = requests.post(url, json.dumps(data), headers=self.heda)
        self.assertEqual("处理成功", response.json().get("message"))

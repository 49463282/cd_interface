# coding=utf-8
import requests
import unittest
import app
from tools.Redis import DBRedis
from tools.PyMysql_cd import DBUtil
import json

url = app.PRE_URL + "/miniapp/orderreturn/add"
list = ["D738042020073121030448413"]
for order_code in list:
    sql = 'select user_id from t_order where order_code = "%s"' % order_code
    database = 'cd_order'
    r = DBUtil.product(sql, database)
    userId = DBUtil.fetch(r, 'fetchone')
    userId = int(userId[0])
    # 查询用户token
    ro = DBRedis.get_connect()
    user = ('user:security:userId:508:%d') % userId
    print(user)
    token = ro.get(user)
    print(token)
    sql = 'select id,spec_id from t_order_detail where order_code = "%s"' % order_code
    r = DBUtil.product(sql, database)
    re = DBUtil.fetch(r, 'fetchone')
    detailId = re[0]
    specId = re[1]
    data = {"type": 1, "explain": "", "orderCode": order_code, "specId": 'specId',
            "detailId": 'detailId', "applyNumber": 1, "evidencePic": "", "reason": 2, "v": "2.6.0"}
    headers = {
        "token": token,
        "Content-Type": "application/json;charset=UTF-8"
    }
    response = requests.post(url, json.dumps(data), headers=headers)
    print(response.text)
    assert 200, response.json().get("status")


class ApiOrder(unittest.TestCase):

    def api_orderreturn_add(self):
        url = app.PRE_URL + "/miniapp/orderreturn/add"
        list = ["D738042020073121030448413",
                "D738042020073121030311949",
                "D738042020073121030267931",
                "D738042020073121030118196",
                "D738042020073121024228677",
                "D738042020073121024137758",
                "D286272020073121024064192",
                "D286272020073121023727261",
                "D286272020073121022419049",
                "D286272020073121021936672",
                "D187882020073121021979528",
                "D738042020073121021577445",
                "D738042020073121021521597",
                "D738042020073121020800271",
                "D738042020073121020809252",
                "D738042020073121020795983",
                "D738042020073121020727351",
                "D738042020073121020680839",
                "D738042020073121020613255",
                "D738042020073121020555237",
                "D187882020073121020417103",
                "D738042020073121020283692",
                "D738042020073121020107032",
                "D187882020073121015912851",
                "D738042020073121015853964",
                "D187882020073121015467172"]
        for order_code in list:
            sql = 'select user_id from t_order where order_code = "%d"' % order_code
            database = 'cd_order'
            r = DBUtil.product(sql, database)
            userId = DBUtil.fetch(r, 'fetchone')
            sql = 'select user_id from t_order_detail where order_code = "%d"' % order_code
            r = DBUtil.product(sql, database)
            re = DBUtil.fetch(r, 'fetchone')
            print(re)
            data = {"type": 1, "explain": "", "orderCode": order_code, "specId": "210508629",
                    "detailId": "1224749", "applyNumber": 1, "evidencePic": "", "reason": 2, "v": "2.6.0"}
            # 查询用户token
            token = r.get('user:security:userId:508:%s') % userId
            headers = {
                "token": token,
                "Content-Type": "application/json;charset=UTF-8"
            }

import requests
import app
import os
import json
import unittest
from tools.PyMysql_cd import DBUtil
from tools.Pandas import Excel


class ApiOpen(unittest.TestCase):
    # def setUp(self):

    def api_open_login(self):
        url = app.BASE_OPEN_URL + "/openapi/auth/login"
        data = {"username": "admin", "password": "111111"}
        response = requests.post(url, data=json.dumps(data), headers=app.headers)
        self.assertEqual(200, response.json().get("status"))
        token = response.json().get("data").get("token")
        app.headers["token"] = token

    def api_update_account_id(self):
        url = app.BASE_OPEN_URL + "/openapi/store/update_account_id"
        excel = Excel()
        io = app.ABS_DIR + "\\data\\account.xlsx"
        df = excel.excel_reade(io, sheet_name="特步子账户绑定")
        if app.BASE_OPEN_URL == "http://apipre.icaodong.com":
            data = [row for row in zip(df["store_name"], df["account_id"])]
            for store_name, account_id in data:
                sql = f"select id,tenant_id from t_store where name ='{store_name}' " \
                      f"and is_deleted = 0 and tenant_id = 508"
                re = DBUtil.cursor(sql, app.userDB)
                results = DBUtil.fetch(re, "fetchone")
                store_id = int(results[0])
                data = {"accountId": account_id, "storeId": store_id, "tenantId": 508}
                response = requests.post(url, data=json.dumps(data), headers=app.headers)
                print(response.text)
                self.assertEqual(200, response.json().get("status"))
        elif app.BASE_OPEN_URL == "http://ir.zlf.cn":
            data = [row for row in zip(df["store_id"], df["account_id"])]
            for store_id, account_id in data:
                data = {"accountId": account_id, "storeId": store_id, "tenantId": 508}
                response = requests.post(url, data=json.dumps(data), headers=app.headers)
                print(response.text)
                self.assertEqual(200, response.json().get("status"))


if __name__ == '__main__':
    open = ApiOpen()
    open.api_open_login()
    open.api_update_account_id()

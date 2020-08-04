# coding=utf-8
import os
import unittest
import requests
from tools.PyMysql_cd import DBUtil
import app_tool
from tools.Request import Request
import time
import json
import csv
from tools.CSV import CSV
from api.ApiProuuct import ApiProduct
from api.ApiUser import ApiUser


class TestProduct(unittest.TestCase):

    # 初始化请求头
    def setUp(self):
        self.headers = {
            "token": app_tool.TOKEN,
            "Content-Type": "application/json;charset=UTF-8"
        }
        self.ApiProduct = ApiProduct()
        self.ApiUser = ApiUser()

    def test_product_add(self):  # 添加商品
        response = self.ApiProduct.api_product_add(self.headers)
        r = self.test_product_list()
        self.assertEqual(r.json().get("data").get("dataList")[0].get("name"), "product_name")
        global prodcutId
        prodcutId = r.json().get("data").get("dataList")[0].get("id")
        self.assertEqual("处理成功", response.json().get("message"))

    def test_product_list(self):
        response = self.ApiProduct.api_product_list(self.headers)
        self.assertEqual(200, response.json().get("status"))
        return response

    def test_product_addstoreproduct(self):  # 选择同步商品到门店
        r = self.ApiUser.api_store_get_sysuser_store_tree(self.headers)
        companyId = str(r.json().get("data")[0].get("id"))
        response = self.ApiProduct.api_product_addstoreproduct(prodcutId, companyId, self.headers)
        r1 = self.ApiProduct.api_storeproduct_list(companyId, self.headers)
        self.assertEqual(200, response.json().get("status"))
        self.assertEqual(r1.json().get("data").get("dataList")[0].get("name"), 'product_name')

    def test_storeproduct_delete(self):
        response = self.ApiProduct.api_storeproduct_delete(prodcutId, self.headers)
        self.assertEqual("仅分公司权限 可操作", response.json().get("message"))

    def test_product_delete(self):
        response = self.ApiProduct.api_product_delete(prodcutId, self.headers)
        self.assertEqual("处理成功", response.json().get("message"))


    # 上架门店商品
    def test_on_updatebatchproduct(self):
        data = {"pidList": productId, "status": 1, "companyIdList": companyId}
        url = app_tool.BASE_URL + "/manager/storeproduct/updatebatchproduct"
        response = requests.post(url, json.dumps(data), headers=self.hade)
        self.assertEqual("处理成功", response.json().get("message"))

    # 下架门店商品
    # def test_the_updatebatchproduct(self):
    #     data = {"pidList": productId, "status": 0, "companyIdList": self.companyIds}
    #     url = app.BASE_URL + "/manager/storeproduct/updatebatchproduct"
    #     response = requests.post(url, json.dumps(data), headers=self.hade)
    #     self.assertEqual("成功", response.json().get("message"))

# coding=utf-8
import os
import unittest
import requests
from tools.PyMysql_cd import DBUtil
import app
from tools.Request import Request
import time
import json
import csv
from tools.CSV import CSV
from api.ApiUser import *


class ApiProduct(unittest.TestCase):

    # 初始化请求头
    def setUp(self):
        self.hade = {
            "token": app.TOKEN,
            "Content-Type": "application/json;charset=UTF-8"
        }

    def api_product_add(self, headers):  # 添加商品
        data = {"name": 'product_name',
                "categoryList": [],
                "labelList": [],
                "materialMainList": [{"id": 12638, "rank": 1}],
                "materialnotMainList": [],
                "details": 'product_name',
                "showImages": "",
                "productCode": "",
                "weight": "0",
                "volume": "0",
                "virtualTotal": "",
                "type": 1,
                "status": 0,
                "isOpen": 1,
                "commissionRulesDTO": {"empAmount": "1", "empPercent": "", "empType": 2, "empSwitch": 1, "id": ""},
                "expressFree": 1,
                "attributeList": [{"key": "颜色",
                                   "value": [{"values": "黄色", "img": ""}], "isShow": 1},
                                  {"key": "尺寸",
                                   "value": [{"values": "160cm", "img": ""}], "isShow": 1}],
                "specificationList": [
                    {"id": "",
                     "imgUrl": "",
                     "inventory": "99",
                     "prePrice": "199",
                     "price": "99",
                     "specCode": "",
                     "specContent": "红色，150cm",
                     "status": 1}],
                "batch": {"prePrice": "199",
                          "price": "99",
                          "inventory": "99"},
                "isVip": 1}
        url = app.BASE_URL + "/manager/product/add"
        response = requests.post(url, json.dumps(data), headers=headers)
        return response

    # 查询商品库商品列表
    def api_product_list(self, headers):
        url = app.BASE_URL + '/manager/product/list'
        data = {"productCode": "", "specCode": "", "name": "", "storeStatus": "", "categoryIds": "", "labelIds": "",
                "typeIds": "", "pageNum": 1, "pageSize": 10}
        response = requests.post(url, json.dumps(data), headers=headers)
        return response

    # 选择商品到分公司
    def api_product_addstoreproduct(self, productId, companyId, headers):  # 选择同步商品到门店
        url = app.BASE_URL + "/manager/product/addstoreproduct"
        data = {"pids": [int(productId)], "mark": 1, "companyIds": [int(companyId)]}
        response = requests.post(url, json.dumps(data), headers=headers)
        return response

    # 查询分公司、门店商品列表
    def api_storeproduct_list(self, companyId, headers):
        url = app.BASE_URL + "/manager/storeproduct/list" + "?productCode=&specCode=&name=&inventory=&categoryIds=&companyId=" \
              + companyId + "&storeId=&status=&typeIds=&labelIds=&pageNum=1&pageSize=10"
        response = requests.get(url, headers=headers)
        return response

    # 删除分公司商品
    def api_storeproduct_delete(self, productId, headers):
        url = app.BASE_URL + "/manager/storeproduct/delete_company_product" + "?productId=" + str(productId)
        response = requests.get(url, headers=headers)
        return response

    def api_product_delete(self, productId, headers):
        url = app.BASE_URL + "/manager/product/delete" + "?productId=" + str(productId)
        response = requests.get(url, headers=headers)
        return response

    # 上架门店商品
    def api_on_updatebatchproduct(self, productId, companyId, headers):
        data = {"pidList": productId, "status": 1, "companyIdList": companyId}
        url = app.BASE_URL + "/manager/storeproduct/updatebatchproduct"
        response = requests.post(url, json.dumps(data), headers=headers)
        self.assertEqual("处理成功", response.json().get("message"))

    # 下架门店商品
    # def test_the_updatebatchproduct(self):
    #     data = {"pidList": productId, "status": 0, "companyIdList": self.companyIds}
    #     url = app.BASE_URL + "/manager/storeproduct/updatebatchproduct"
    #     response = requests.post(url, json.dumps(data), headers=self.hade)
    #     self.assertEqual("成功", response.json().get("message"))

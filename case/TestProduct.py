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


class TestProduct(unittest.TestCase):

    # 初始化请求头
    def setUp(self):
        self.hade = {
            "token": app.TOKEN,
            "Content-Type": "application/json;charset=UTF-8"
        }

    def readCSV(self, filename):
        '''
        :param filename: 需要读取的数据文件
        :return: [{data1},{data2}...]
        '''
        try:
            datas = []
            # 以DictReader的方式读取数据文件，方便与json互做转换
            with open(filename, 'r') as csvfile:
                # 从文件里读取到的数据转换成字典列表的格式
                reader = csv.DictReader(csvfile)
                for row in reader:
                    data = {}
                    data['id'] = row['id']
                    data['method'] = row['method']
                    data['mark'] = row['mark']
                    data['companyIds'] = str(row['companyIds'])
                    data['expressFree'] = str(row['expressFree'])
                    data['isVip'] = str(row['isVip'])
                    data['inventory'] = row['inventory']
                    data['shareTotal'] = row['shareTotal']
                    data['expect'] = json.dumps(row['expect']) \
                        if isinstance(row['expect'], dict) \
                        else row['expect']
                    datas.append(data)
                return datas
        except FileNotFoundError:
            return datas

    def test_product_add(self):
        data = {"name": "接口测试", "categoryList": [], "labelList": [], "materialMainList": [{"id": 12638, "rank": 1}],
                "materialnotMainList": [], "details": "接口测试", "showImages": "", "productCode": "", "weight": "0",
                "volume": "0", "virtualTotal": "", "type": 1, "status": 0, "isOpen": 1,
                "commissionRulesDTO": {"empAmount": "1", "empPercent": "", "empType": 2, "empSwitch": 1, "id": ""},
                "expressFree": 1, "attributeList": [{"key": "颜色",
                                                     "value": [{"values": "红色", "img": ""}, {"values": "绿色", "img": ""},
                                                               {"values": "黄色", "img": ""}], "isShow": 1}, {"key": "尺寸",
                                                                                                            "value": [{
                                                                                                                "values": "150cm",
                                                                                                                "img": ""},
                                                                                                                {
                                                                                                                    "values": "160cm",
                                                                                                                    "img": ""}],
                                                                                                            "isShow": 1}],
                "specificationList": [
                    {"id": "", "imgUrl": "", "inventory": "99", "prePrice": "199", "price": "99", "specCode": "",
                     "specContent": "红色，150cm", "status": 1},
                    {"id": "", "imgUrl": "", "inventory": "99", "prePrice": "199", "price": "99", "specCode": "",
                     "specContent": "红色，160cm", "status": 1},
                    {"id": "", "imgUrl": "", "inventory": "99", "prePrice": "199", "price": "99", "specCode": "",
                     "specContent": "绿色，150cm", "status": 1},
                    {"id": "", "imgUrl": "", "inventory": "99", "prePrice": "199", "price": "99", "specCode": "",
                     "specContent": "绿色，160cm", "status": 1},
                    {"id": "", "imgUrl": "", "inventory": "99", "prePrice": "199", "price": "99", "specCode": "",
                     "specContent": "黄色，150cm", "status": 1},
                    {"id": "", "imgUrl": "", "inventory": "99", "prePrice": "199", "price": "99", "specCode": "",
                     "specContent": "黄色，160cm", "status": 1}],
                "batch": {"prePrice": "199", "price": "99", "inventory": "99"}, "isVip": 1}
        url = app.BASE_URL + "/manager/product/add"
        response = requests.post(url, json.dumps(data), headers=self.hade)
        # print(response.text)
        self.assertEqual("成功", response.json().get("message"))

    # 选择同步商品到门店
    def test_product_addstoreproduct(self):
        # 查询新增的商品id
        database = "cd-product_uat"
        conn = DBUtil.get_connect(database)
        cursor = DBUtil.get_cursor(conn)
        sql = 'select id from t_product where name = "接口测试" and tenant_id = 100 and `status` = 0'
        cursor.execute(sql)
        r = cursor.fetchone()
        self.id = str(r[0])
        DBUtil.close_res(cursor, conn)
        id = []
        str_id = str(self.id)
        id.append(str_id)
        c = list(map(eval, id))
        # 选择商品到分公司
        url = app.BASE_URL + "/manager/product/addstoreproduct"
        data = {"pids": c, "mark": 1, "companyIds": [27099]}
        requests.post(url, json.dumps(data), headers=self.hade)
        # 调用assert方法，检查预期结果是否在响应结果中存在
        database = "cd-product_uat"
        conn = DBUtil.get_connect(database)
        cursor = DBUtil.get_cursor(conn)
        DBUtil.close_res(cursor, conn)
        sql = "select inventory from t_store_product where name = '接口测试' and tenant_id = 100"
        cursor.execute(sql)
        r = cursor.fetchone()
        DBUtil.close_res(cursor, conn)
        inventory = str(r[0])
        self.assertEqual(inventory, str(594))
        # print(inventory)
        # 获取测试用例的路径
        data_file = os.path.abspath("data") + "\\product_addstoreproduct.csv"
        # 指定最终结果生成的数据文件名称
        result_file = os.path.abspath("report") + "\\addstoreproduct_{}.csv".format(str(time.time()).split(".")[0])
        data = self.readCSV(data_file)
        # 数据文件有内容则调用接口，否则直接测试结束
        if data.__len__() > 0:
            results = []
            for testcase in data:
                result = {}
                companyIds = []
                companyIds.append(testcase["companyIds"])
                result["id"] = testcase["id"]
                result["method"] = testcase["method"]
                result["mark"] = int(testcase["mark"])
                result["companyIds"] = list(map(eval, companyIds))
                result["expressFree"] = int(testcase["expressFree"])
                result["isVip"] = int(testcase["isVip"])
                result["inventory"] = int(testcase["inventory"])
                result["shareTotal"] = int(testcase["shareTotal"])
                result["expect"] = testcase["expect"]
                # 组装参数
                id = []
                str_id = str(self.id)
                id.append(str_id)
                b = map(eval, id)
                # 被“list”后的b将清空
                self.c = list(b)
                self.companyIds = result["companyIds"]
                params = {
                    "pids": self.c,
                    "mark": result["mark"],
                    "companyIds": result["companyIds"],
                    "expressFree": result["expressFree"],
                    "isVip": result["isVip"],
                    "inventory": result["inventory"],
                    "shareTotal": result["shareTotal"],
                }
                url = app.BASE_URL + "/manager/product/addstoreproduct"
                response = Request().httprequest(result["method"], url, params, self.hade)
                # 调用assert方法，检查预期结果是否在响应结果中存在
                database = "cd-product_uat"
                conn = DBUtil.get_connect(database)
                cursor = DBUtil.get_cursor(conn)
                DBUtil.close_res(cursor, conn)
                sql = "select inventory,express_free from t_store_product where name = '接口测试' and tenant_id = 100"
                cursor.execute(sql)
                r = cursor.fetchone()
                DBUtil.close_res(cursor, conn)
                inventory = str(r[0]) + "," + str(r[1])
                assert_value = CSV().assertResult(result["expect"], inventory)
                result["real_value"] = response.text
                result["assert_value"] = assert_value
                # 获取每一行里的所有字段以及实际结果和验证结果
                results.append(result)
                # 执行完所有记录后，将所有结果写入result.csv
                headers = "id,method,mark,companyIds,expressFree,isVip,inventory,shareTotal,expect,real_value,assert_value".split(
                    ",")
                CSV().writeCSV(result_file, results, headers)  # 写入csv文件

    def test_product_delete(self):
        database = "cd-product_uat"
        conn = DBUtil.get_connect(database)
        cursor = DBUtil.get_cursor(conn)
        sql = 'select id from t_product where name = "接口测试" and tenant_id = 100 and `status` = 0'
        cursor.execute(sql)
        r = cursor.fetchone()
        self.id = str(r[0])
        response = requests.get(app.BASE_URL + "/manager/product/delete?productId=" + self.id, self.hade)
        self.assertEqual("成功", response.json().get("message"))

    def test_on_updatebatchproduct(self):
        # self.test_product_addstoreproduct()
        data = {"pidList": self.c, "status": 1, "companyIdList": self.companyIds}
        url = app.BASE_URL + "/manager/storeproduct/updatebatchproduct"
        response = requests.post(url, json.dumps(data), headers=self.hade)
        self.assertEqual("成功", response.json().get("message"))

    def test_the_updatebatchproduct(self):
        # self.test_product_addstoreproduct()
        data = {"pidList": self.c, "status": 0, "companyIdList": self.companyIds}
        url = app.BASE_URL + "/manager/storeproduct/updatebatchproduct"
        response = requests.post(url, json.dumps(data), headers=self.hade)
        self.assertEqual("成功", response.json().get("message"))

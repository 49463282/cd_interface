# coding=utf-8
import requests
import json
import app


class Order:
    def __init__(self):
        self.url = app.BASE_URL + '/manager/store/get_sysuser_store'
        data = {"pageNum": 1, "pageSize": 10, "createBeginTime": "", "createEndTime": "",
                "orderCode": "D537422020031811580974545", "orderType": "", "payBeginTime": "", "payEndTime": "",
                "productName": "", "receiverName": "", "receiverPhone": "", "userName": "", "orderStatus": 0,
                "storeId": "",
                "companyId": "", "isTake": ""}
        # 请求头
        self.heda = {
            "token": app.TOKEN,
            "Content-Type": "application/json;charset=UTF-8"
        }
        self.data = json.dumps(data)

    def get_order_list(self):
        return requests.get(self.url, data=self.data, headers=self.heda)

# coding=utf-8
import requests
import json


class Request():
    def httprequest(self, method, url, param, headers):
        if method.upper() == "GET":
            return requests.get(url, json.dumps(param), headers=headers)
        elif method.upper() == "POST":
            return requests.post(url, json.dumps(param), headers=headers)

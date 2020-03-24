# coding=utf-8
import requests
import json


class Request():
    def httprequest(self, method, url, param, head):
        if method.upper() == "GET":
            return requests.get(url, json.dumps(param), headers=head)
        elif method.upper() == "POST":
            return requests.post(url, json.dumps(param), headers=head)

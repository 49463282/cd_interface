import requests
import json
import app

class Login:
    def __init__(self):
        self.url = app.BASE_URL + '/manager/sysuser/login'

    def get_login(self,code):
        data = {"tenantId": 100, "mobile": "18549811213", "password": "qwe123", "code": code,
                "uuid": "1e4cfdb3-ba66-4082-892b-13ba4059436d", "brandType": 1, "type": 0}
        heda = {
            "token": app.TOKEN,
            "Content-Type": "application/json;charset=UTF-8"
        }
        self.data = json.dumps(data)
        self.data = json.dumps(data)
        return requests.post(self.url, data=self.data, headers=heda)

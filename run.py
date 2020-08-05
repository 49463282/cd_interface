from flask import Flask, render_template, request, make_response, redirect
import requests
import app_tool
from tools.Redis import DBRedis
from tools.PyMysql_cd import DBUtil
import json

app = Flask(__name__, template_folder='t', static_url_path='/static', static_folder='s')


@app.route('/')
def form_views():
    return render_template('03-form.html')


@app.route('/order_return')
def form_do():
    if request.method == 'GET':
        # 获取 form 表单提交过来的数据
        order_code = request.args.get('order_code')
        print('订单编号:%s' % (order_code))
        url = app_tool.BASE_URL + "/miniapp/orderreturn/add"
        list = [order_code]
        for order_code in list:
            sql = 'select user_id,tenant_id from t_order where order_code = "%s"' % order_code
            r = DBUtil.product(sql, app_tool.orderDB)
            I = DBUtil.fetch(r, 'fetchone')
            userId = int(I[0])
            tenantId = int(I[1])
            # 查询用户token
            ro = DBRedis.get_connect()
            user = ('user:security:userId:%d:%d') % (tenantId, userId)
            token = ro.get(user)
            sql = 'select id,spec_id from t_order_detail where order_code = "%s"' % order_code
            r = DBUtil.product(sql, app_tool.orderDB)
            re = DBUtil.fetch(r, 'fetchone')
            detailId = str(re[0])
            specId = str(re[1])
            data = {"type": 1, "explain": "", "orderCode": order_code, "specId": specId,
                    "detailId": detailId, "applyNumber": 1, "evidencePic": "", "reason": 2, "v": "2.6.0"}
            headers = {
                "token": token,
                "Content-Type": "application/json;charset=UTF-8"
            }
            response = requests.post(url, json.dumps(data), headers=headers)
            assert 200, response.json().get("status")
            return render_template('03-form.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)

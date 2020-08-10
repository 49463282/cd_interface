from flask import Flask, render_template, request, make_response, redirect
import requests
import app
from tools.Redis import DBRedis
from tools.PyMysql_cd import DBUtil
import json

app_tool = Flask(__name__, template_folder='t', static_url_path='/static', static_folder='s')


def form_views():
    return render_template('03-form.html')


@app_tool.route('/order_return')
def from_views():
    return render_template("order_return_type.html")


@app_tool.route('/order_return_type')
def form_return_type():
    if request.method == "GET":
        return_code = request.args.get("return_code")
        sql = 'select refund_type from t_order_return where return_code = "%s";' % return_code
        r = DBUtil.product(sql, app.orderDB)
        I = DBUtil.fetch(r, 'fetchone')
        return_type = int(I[0])
        if return_type == 1:
            type = "为线上退款"
        elif return_type == 2:
            type = "为线下退款"
    return render_template("order_return_type.html", return_type=type, return_code=return_code)


@app_tool.route('/order_return')
def form_do():
    if request.method == 'GET':
        # 获取 form 表单提交过来的数据
        order_code = request.args.get('order_code')
        print('订单编号:%s' % (order_code))
        url = app.BASE_URL + "/miniapp/orderreturn/add"
        list = [order_code]
        for order_code in list:
            sql = 'select user_id,tenant_id from t_order where order_code = "%s"' % order_code
            r = DBUtil.product(sql, app.orderDB)
            I = DBUtil.fetch(r, 'fetchone')
            userId = int(I[0])
            tenantId = int(I[1])
            # 查询用户token
            ro = DBRedis.get_connect()
            user = ('user:security:userId:%d:%d') % (tenantId, userId)
            token = ro.get(user)
            sql = 'select id,spec_id from t_order_detail where order_code = "%s"' % order_code
            r = DBUtil.product(sql, app.orderDB)
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
    app_tool.run(host="0.0.0.0", debug=True, port=5000)

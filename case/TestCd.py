import unittest
from api.OrderApi import Order
from api.pymysql_cd import DBUtil


class TestCd(unittest.TestCase):

    # 初始化与销毁
    def setUp(self):
        self.order = Order()

    def test_order(self):
        # 指定连接的数据库
        database = 'cd-user_uat'
        # 调用请求业务
        response = self.order.get_order_list()
        # 断言判断
        self.assertEqual('成功', response.json().get("message"))
        conn = DBUtil.get_connect(database)
        cursor = DBUtil.get_cursor(conn)
        sql = "select * from t_user where mobile = 18549811213 and type = 0"
        cursor.execute(sql)
        ro = cursor.fetchall()
        for r in ro:
            print(r)
        DBUtil.close_res(cursor, conn)

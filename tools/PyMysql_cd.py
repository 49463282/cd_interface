# coding=utf-8
import pymysql


class DBUtil:
    @classmethod
    def get_connect(cls, database):
        return pymysql.connect(host='134.175.210.250', user='cdmall', password='cdMall@321', database=database,
                       charset='utf8')

    @classmethod
    def get_cursor(cls, conn):
        return conn.cursor()

    @classmethod
    def close_res(cls, cursor, conn):
        if cursor:
            cursor.close
            cursor = None
        if conn:
            conn.close
            conn = None


# conn = pymysql.connect(host='134.175.210.250', user='cdmall', password='cdMall@321', database='cd-product_uat',
#                        charset='utf8')
# cursor = conn.cursor()
# sql = 'select id from t_product where name = "接口测试" and tenant_id = 100 and `status` = 0 group by create_time desc limit 1'
# cursor.execute(sql)
# data = cursor.fetchone()
# print(data)
# print(type(data))
# r = data[0]
# print(r)
# if r == 15730:
#     print(True)
# else:
#     print(False)

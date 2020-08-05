# coding=utf-8
import pymysql
import app

class DBUtil:
    @classmethod
    def get_connect(cls, database):
        # 测试数据库
        if app.BASE_URL == "http://apiuat.icaodong.com":
            return pymysql.connect(host='134.175.210.250', user='cdmall', password='cdMall@321', database=database,
                                   charset='utf8')
        # 生产数据库
        elif app.BASE_URL == "http://apipre.icaodong.com":
            return pymysql.connect(host='134.175.220.145', user='test_read', password='test_read@20200604',
                                   database=database, port=23305,
                                   charset='utf8')
        else:
            return "配置文件填写的请求地址不正确"
    @classmethod
    def get_cursor(cls, conn):
        return conn.cursor()

    @classmethod
    def product(cls, sql, database):
        conn = DBUtil.get_connect(database)
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor
        # if number == 'fetchone':
        #     return cursor.fetchone()
        # if number == 'all':
        #     return cursor.all()
        # else:
        #     return '正确填写获取的数量'

    @classmethod
    def fetch(cls, results, number):
        if number == 'fetchone':
            return results.fetchone()
        if number == 'all':
            return results.all()
        else:
            return '正确填写获取的数量'

    @classmethod
    def close_res(cls, cursor, conn):
        if cursor:
            cursor.close
            cursor = None
        if conn:
            conn.close
            conn = None

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
    def product(cls, sql):
        database = "cd-product_uat"
        conn = DBUtil.get_connect(database)
        cursor = DBUtil.get_cursor(conn)
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

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

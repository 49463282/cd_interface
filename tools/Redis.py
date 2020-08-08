# coding=utf-8
import redis
import app
from data import redis_data


class DBRedis:
    @classmethod
    def get_connect(cls):
        # 测试Redis库
        if app.BASE_URL == "http://apiuat.icaodong.com":
            return redis.StrictRedis(host='134.175.210.250', port=65379, password='cdMall@321', db=5,
                                     decode_responses=True)

        # 生产 Redis库
        elif app.BASE_URL == "http://apipre.icaodong.com":
            return redis.StrictRedis(host='134.175.210.250', port=26379,
                                     password='jzkj@2018redis', db=6,
                                     decode_responses=True)

# coding=utf-8
import redis


class DBRedis:
    @classmethod
    def get_connect(cls):
        # return redis.StrictRedis(host='134.175.210.250', port=65379, password='cdMall@321', db=, decode_responses=True)

        return redis.StrictRedis(host='134.175.210.250', port=65379, password='cdMall@321', db=, decode_responses=True)

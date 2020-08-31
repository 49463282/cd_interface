# coding=utf-8
import os

TOKEN = None
# url
# BASE_URL = "http://apipre.icaodong.com"
BASE_URL = "http://apiuat.icaodong.com"
# BASE_URL = "http://182.254.167.77"
BASE_OPEN_URL = "http://apipre.icaodong.com"


# BASE_OPEN_URL = "http://ir.zlf.cn"

def base_url(base):
    base_url = {
        "pre": "http://apipre.icaodong.com",
        "uat": "http://apiuat.icaodong.com",
        "open": "http://apipre.icaodong.com"
    }
    return base_url[base]


headers = {
    "token": TOKEN,
    "Content-Type": "application/json;charset=UTF-8"
}
# 获取资源的绝对路径
ABS_PATH = os.path.abspath(__file__)
# 获取项目的绝对路径
ABS_DIR = os.path.dirname(ABS_PATH)

# 连接的数据库库名
if BASE_URL == "http://apiuat.icaodong.com":
    userDB = "cd-user_uat"
    systemDB = "cd-system_uat"
    salesDB = "cd-sales_uat"
    productDB = "cd-product_uat"
    orderDB = "cd-order_uat"
elif BASE_URL == "http://apipre.icaodong.com":
    userDB = "cd_user"
    systemDB = "cd_system"
    salesDB = "cd_sales"
    productDB = "cd_product"
    orderDB = "cd_order"

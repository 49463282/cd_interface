# coding=utf-8
import os

# url
BASE_URL = "http://apipre.icaodong.com"
TOKEN = None
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

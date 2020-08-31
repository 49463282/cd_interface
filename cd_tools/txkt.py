import let as let
from selenium import webdriver
import time
import json
from selenium.webdriver.common.action_chains import ActionChains

# 填写webdriver的保存目录
driver = webdriver.Chrome()

# # 记得写完整的url 包括http和https
# driver.get('https://ke.qq.com/')
#
# # 程序打开网页后20秒内手动登陆账户
# time.sleep(20)
#
# with open('cookies.txt', 'w') as cookief:
#     # 将cookies保存为json格式
#     cookief.write(json.dumps(driver.get_cookies()))
# driver.close()
# 记得写完整的url 包括http和https
driver.get('https://ke.qq.com/webcourse/index.html#cid=2727214&term_id=102834325&lite=1&from=800021724')
# 窗口最大化
driver.maximize_window()
# 首先清除由于浏览器打开已有的cookies
driver.delete_all_cookies()

with open('cookies.txt', 'r') as cookief:
    # 使用json读取cookies 注意读取的是文件 所以用load而不是loads
    cookieslist = json.load(cookief)

    # 方法1 将expiry类型变为int
    for cookie in cookieslist:
        # 并不是所有cookie都含有expiry 所以要用dict的get方法来获取
        if isinstance(cookie.get('expiry'), float):
            cookie['expiry'] = int(cookie['expiry'])
        driver.add_cookie(cookie)
# 刷新页面
driver.refresh()


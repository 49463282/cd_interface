import json

from selenium import webdriver
from time import sleep

from selenium.common.exceptions import NoSuchElementException

# driver = webdriver.Chrome()
# driver.get('http://page5.zzu.edu.cn:8080/system/login.jsp')
# '''
# JSESSIONID=24468B3B8DA4195D8E4C1B7A583E74BF;
# weblogintype=cmslogin;
# webcorpname=tyx;
# webskinname=green;
# wb_login_account_set=tyx;
# _newscontentshowADV=true;
# wbcmsshowsysid=mysite'''
# driver.add_cookie({'name': 'JSESSIONID', 'value': '24468B3B8DA4195D8E4C1B7A583E74BF'})
# driver.add_cookie({'name': 'weblogintype', 'value': 'cmslogin'})
# driver.add_cookie({'name': 'webcorpname', 'value': 'tyx'})
# driver.add_cookie({'name': 'webskinname', 'value': 'green'})
# driver.add_cookie({'name': 'wb_login_account_set', 'value': 'tyx'})
# driver.add_cookie({'name': '_newscontentshowADV', 'value': 'true'})
# driver.add_cookie({'name': 'wbcmsshowsysid', 'value': 'mysite'})
# sleep(5)
# driver.quit()
# i = 0
# while 2 > 1:
#     line = 'line_u5_' + str(i)
#     try:
#         name = driver.find_element_by_id(line).text
#         driver.find_element_by_id(line).click()
#         headline = driver.find_element_by_class_name('border').text
#         driver.get('http://www5.zzu.edu.cn/tyx/kxyj.htm')
#         i = int(i) + 1
#     except:
#         i = int(i) + 1
#         line = 'line_u5_' + str(i)
#         driver.get('http://www5.zzu.edu.cn/tyx/kxyj.htm')
#         name = driver.find_element_by_id(line).text
#         driver.find_element_by_id(line).click()
#         headline = driver.find_element_by_class_name('border').text
#         driver.get('http://www5.zzu.edu.cn/tyx/kxyj.htm')
#         if i == 15:
#             break
# finally:

# print(time[-12:-5])
# print(time)
# print(name)
# print(headline)
# print(unit)



# coding=utf-8
import unittest

from case.TestCd import TestCd
from case.TestLogin import TestLogin
from tools.HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import os
from email.mime.multipart import MIMEMultipart
import time

suite = unittest.TestSuite()
case_dir = os.path.join(os.path.abspath(__file__), "C:\\Users\hp\PycharmProjects\\cd_interface\\case\\")
# suite = unittest.TestSuite()
discover = unittest.defaultTestLoader.discover(case_dir,
                                               pattern="Test*.py",
                                               top_level_dir=None)
suite.addTests(discover)  # 直接加载 discover    可以兼容python2和3
# suite.addTest(TestLogin('test_login'))
# suite.addTest(TestCd('test_order'))
# suite.addTest(TestLogin('test_login'))
# suite.addTest(TestCd('test_order'))
# 创建文件（生成的测试报告）

file = "./report/" + time.strftime("%Y-%m-%d" + "%H_%M_%S" + "_result.html")
with open(file, "wb") as f:
    runner = HTMLTestRunner(f, title="草动接口测试报告", description="自动化测试")
    runner.run(suite)

# def all_case():
#     # 待执行用例的目录
#     # case_dir = "C:\\Users\hp\PycharmProjects\\cd_interface\\case\\"
#     # case_dir = os.path.join(os.path.abspath(__file__), "C:\\Users\hp\PycharmProjects\\cd_interface\\case\\")
#     suite = unittest.TestSuite()
#     # discover = unittest.defaultTestLoader.discover(case_dir,
#     #                                                pattern="Test*.py",
#     #                                                top_level_dir=None)
#     # suite.addTests(discover)  # 直接加载 discover    可以兼容python2和3
#     suite.addTest(TestLogin('test_login'))
#     suite.addTest(TestCd('test_order'))
#     return suite
#
#
# # ==============定义发送邮件==========
# def send_mail(report):
#     # -----------1.跟发件相关的参数------
#     smtpserver = 'smtp.qq.com'  # 发件服务器
#     port = 465  # 端口
#     username = '49463282@qq.com'  # 发件箱用户名
#     password = 'brnntqcrqputbhih'  # 发件箱密码
#     sender = '49463282@qq.com'  # 发件人邮箱
#     receiver = ['dingyuanming@wowkai.cn']  # 收件人邮箱
#     # ----------2.编辑邮件的内容------
#     # 读文件
#     f = open(report, 'rb')
#     mail_body = f.read()
#     f.close()
#     # 邮件正文是MIMEText
#     body = MIMEText(mail_body, 'html', 'utf-8')
#     # 邮件对象
#     msg = MIMEMultipart()
#     msg['Subject'] = Header("自动化测试报告", 'utf-8').encode()  # 主题
#     msg['From'] = Header(u'测试机 <%s>' % sender)  # 发件人
#     msg['To'] = Header(u'测试负责人 <%s>' % receiver)  # 收件人
#     msg['To'] = ';'.join(receiver)
#     msg['date'] = time.strftime("%a,%d %b %Y %H:%M:%S %z")
#     msg.attach(body)
#     # 附件
#     att = MIMEText(mail_body, "base64", "utf-8")
#     att["Content-Type"] = "application/octet-stream"
#     att["Content-Disposition"] = 'attachment; filename="test_report.html"'
#     msg.attach(att)
#     # ----------3.发送邮件------
#     try:
#         smtp = smtplib.SMTP()
#         smtp.connect(smtpserver)  # 连服务器
#         smtp.login(sender, password)
#     except:
#         smtp = smtplib.SMTP_SSL(smtpserver, port)
#         smtp.login(username, password)  # 登录
#     smtp.sendmail(sender, receiver, msg.as_string())  # 发送
#     smtp.quit()
#     print("邮件已发出！注意查收。")
#
#
# # ======查找测试目录，找到最新生成的测试报告文件======
# def new_report(report):
#     lists = os.listdir(report)  # 列出目录的下所有文件和文件夹保存到lists
#     lists.sort(key=lambda fn: os.path.getmtime(report + "\\" + fn))  # 按时间排序
#     file_new = os.path.join(report, lists[-1])  # 获取最新的文件保存到file_new
#     return file_new
#
#
# if __name__ == "__main__":
#     # 返回实例
#     # suite = unittest.TextTestRunner()
#     # 导入第三方模块HTMLTestRunner
#     import time
#
#     # 获取当前时间，这样便于下面的使用。
#     now = time.strftime("%Y-%m-%d" + "%H_%M_%S", time.localtime(time.time()))
#     # 保存生成报告的路径
#     report_path = "C:\\Users\hp\PycharmProjects\\cd_interface\\report\\" + now now + "_result.html"
#     fp = open(report_path, 'wb')
#     runner = HTMLTestRunner(stream=fp,
#                             title=u"这是我的自动化测试用例",
#                             description=u"用例执行情况",
#                             verbosity=2
#                             )
#     # run 所有用例
#     runner.run(all_case())
#     # 关闭文件，记住用open()打开文件后一定要记得关闭它，否则会占用系统的可打开文件句柄数。
#     fp.close()
#     # 测试报告文件夹
#     test_path = "C:\\Users\hp\PycharmProjects\\cd_interface\\report\\"
#     new_report = new_report(test_path)
#     send_mail(new_report)  # 发送测试报告

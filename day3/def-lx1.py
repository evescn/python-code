#!/usr/bin/env python
# -*- conding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

# def mail():
#     msg = MIMEText('邮件内容', 'plain', 'utf-8')
#     msg['From'] = formataddr(["evescn", '18111434862@163.com'])
#     msg['To'] = formataddr(["gmkk", '519518995@qq.com'])
#     msg['Subject'] = "主题"
#
#     server = smtplib.SMTP("smtp.163.com", 25)
#     server.login("18111434862@163.com", "GM911025GM")
#     server.sendmail('18111434862@163.com', ['519518995@qq.com', ], msg.as_string())
#     server.quit()
#
# mail()

def mail(mails):
    msg = MIMEText('邮件内容', 'plain', 'utf-8')
    msg['From'] = formataddr(["evescn", '18111434862@163.com'])
    msg['To'] = formataddr(["gmkk", mails])
    msg['Subject'] = "主题"

    server = smtplib.SMTP("smtp.163.com", 25)
    server.login("18111434862@163.com", "GM911025GM")
    server.sendmail('18111434862@163.com', [mails, ], msg.as_string())
    server.quit()

mail('519518995@qq.com')


# f = mail
# f()
# print(ret)
#
# def show():
#     print('a')
#     return [11, 22,]
#     print('b')
#
# show()


# -*- coding: utf-8 -*-
# @Time : 2020/12/9 19:20
# @File : EmailUtil.py
# @Author : Yvon_fajin

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from config.Conf import ConfigYaml
from email.header import Header

email_info = ConfigYaml().get_email_info()

#1.初始化
#2.#smtp地址，用户名，密码，接收邮件者，邮件标题，邮件内容，邮件附件
class SendEmail:
    def __init__(self,smtp_addr,username,password,sender, recv,title,content=None,file=None):
        self.smtp_addr = smtp_addr
        self.username = username
        self.password = password
        self.sender = sender
        self.recv = recv
        self.title = title
        self.content = content
        self.file = file

#3.发送邮件方法
    def send_mail(self):
        #MIME
        msg = MIMEMultipart()
        #初始化邮件信息
        msg.attach(MIMEText(self.content,_charset="utf-8",_subtype='plain'))
        msg["Subject"] = self.title
        msg["From"] = self.sender
        # msg["To"] = self.recv
        msg["To"] = ','.join(self.recv)
        #邮件附件
        #判断是否有附件
        if self.file:
        #MIMEText读取文件
            att = MIMEText(open(self.file).read())
        #设置内容类型
            att["Content-Type"] = "application/octet-stream"
        # 设置附件头
            att["Content-Disposition"] = 'attachment;filename="%s"' % self.file
        #将内容附件到邮件主题中
            msg.attach(att)
        #登录邮件服务器

        self.smtp = smtplib.SMTP()
        self.smtp.connect(self.smtp_addr)
        self.smtp.login(self.username, self.password)

        try:
            self.smtp.sendmail(self.sender, self.recv, msg.as_string())
            # self.smtp.quit()
            print('成功了。。')
        except Exception as e:
            print('出错了..', e)


if __name__ == "__main__":
    smtp_addr = email_info["smtpserver"]
    username = email_info["username"]
    password = email_info["password"]
    sender = email_info["sender"]
    to_receiver = email_info["to_receiver"]
    cc_receiver = email_info["cc_receiver"]
    recv = to_receiver.split(',') + cc_receiver.split(',')

    print(recv)

    email = SendEmail(smtp_addr, username, password, sender,recv, "通知邮件")
    email.send_mail()


"""
#封装公共方法

"""



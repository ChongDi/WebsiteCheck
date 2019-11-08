import time
import os
from lxml import html
import datetime
import requests
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def CheckTheWebsite(url):
    page = requests.get(url)
    tree = html.fromstring(page.content)
    o_date = tree.xpath('//span/text()')
    o_title = tree.xpath('//a[@style="overflow-x:hidden;"]/text()')
    o_link = tree.xpath('//a[@style="overflow-x:hidden;"]/@href')
    date = o_date[-len(o_title):]
    title = o_title
    link = o_link
    return date, title, link

def email(TEXT, HLink):

    sender = 'XXX@163.com'#填写发件人
    pwd = 'XXX'#密码（SMTP授权密码，详见邮箱相关设置）
    receivers = ['807165827@qq.com']#填写收件人     
    MainTEXT = "你好，网站有内容更新，请及时查看:"+TEXT+'\n'+HLink
    message = MIMEText(MainTEXT,"plain",'utf-8')
    # 三个参数：第一个为文本内容，第二个为plain设置文本格式，第三个为utf-8设置编码
    message ['From'] = "XXX <XXX@163.com>"
    message ['To'] = "XXX <XXX@qq.com>"

    subject = "学生办网站: "+TEXT
    #邮件主题
    message["Subject"] = subject

    try:
        # 使用非本地服务器，需要建立ssl连接
        smtpObj = smtplib.SMTP_SSL("smtp.163.com",465)
        #发件箱邮件服务器
        smtpObj.login(sender,pwd)
        smtpObj.sendmail(sender,receivers,message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print("Error：无法发送邮件.Case:%s"%e)

#目标跟踪网页
url_1 = 'http://xsb.seiee.sjtu.edu.cn/xsb/list/611-1-20.htm'
url_2 = 'http://xsb.seiee.sjtu.edu.cn/xsb/list/1981-1-20.htm'
url_3 = 'http://xsb.seiee.sjtu.edu.cn/xsb/list/2676-1-20.htm'

Message_1 = []
Message_sent_1 = []
Message_2 = []
Message_sent_2 = []
Message_3 = []
Message_sent_3 = []

while True:
    today = '['+str(datetime.date.today())+']'

    #奖学金
    [date, title, link] = CheckTheWebsite(url_1)
    for num, item in enumerate(date):
        if item == today: #For test, shoule be item == today
            Message_1 = []
            Message_1.append(title[num])
            Link_1 = []
            hlink = 'http://xsb.seiee.sjtu.edu.cn'+link[num]
            Link_1.append(hlink)

    if len(Message_1) and Message_1 != Message_sent_1:    #Send an e-mail iff there is an update today
        TEXT = '奖学金: '
        for item in Message_1:
            TEXT = TEXT+item+'; '
        HLink = ''
        for item in Link_1:
            HLink = HLink+item+'\n'
        email(TEXT,HLink)
        Message_sent_1 = Message_1.copy()
    #讲座活动
    [date, title, link] = CheckTheWebsite(url_2)
    for num, item in enumerate(date):
        if item == today: #For test, shoule be item == today
            Message_2 = []
            Message_2.append(title[num])
            Link_2 = []
            hlink = 'http://xsb.seiee.sjtu.edu.cn'+link[num]
            Link_2.append(hlink)

    if len(Message_2) and Message_2 != Message_sent_2:    #Send an e-mail iff there is an update today
        TEXT = '讲座活动: '
        for item in Message_2:
            TEXT = TEXT+item+'; '
        HLink = ''
        for item in Link_2:
            HLink = HLink+item+'\n'
        email(TEXT,HLink)
        Message_sent_2 = Message_2.copy()
    #党团活动
    [date, title, link] = CheckTheWebsite(url_3)
    for num, item in enumerate(date):
        if item == today: #For test, shoule be item == today
            Message_3 = []
            Message_3.append(title[num])
            Link_3 = []
            hlink = 'http://xsb.seiee.sjtu.edu.cn'+link[num]
            Link_3.append(hlink)

    if len(Message_3) and Message_3 != Message_sent_3:    #Send an e-mail iff there is an update today
        TEXT = '党团活动: '
        for item in Message_3:
            TEXT = TEXT+item+'; '
        HLink = ''
        for item in Link_3:
            HLink = HLink+item+'\n'
        email(TEXT,HLink)
        Message_sent_3 = Message_3.copy()
    time.sleep(3600)

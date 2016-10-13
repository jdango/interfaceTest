#encoding=utf-8
'''
@note:对邮件的统一操作
@author: eason.sun
@organization: csb
@copyright: weiyao
'''
import smtplib
from email.header import Header
import email.MIMEMultipart
import os.path
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from Util.File import Config



def send_email(content, header,  rev_addr_lst,
                            host= Config.DefaultConfig().Email.Domain,
                            username= Config.DefaultConfig().Email.Sender,
                            password= Config.DefaultConfig().Email.Password, 
                            sender_addr= Config.DefaultConfig().Email.Sender ):
    """
    @author: eason.sun
    @content:邮件发送的主要内容
    @header:邮件发送的头部
    @username:邮件发件人账号
    @password:邮件发件人账号密码
    @sender_addr:邮件发送时，发件人显示地址
    @rev_addr_lst:收件人列表    
    
    @return: None
    
    @summary: 用于发送邮件内容，内容仅限文本内容
    """
    send_msg = MIMEText(content, _subtype = "html", _charset = "utf-8")
    send_msg["Subject"] = Header(header, "utf-8")
    smtp = smtplib.SMTP()
    smtp.connect(host)
    smtp.login(username, password)
    smtp.sendmail(sender_addr, rev_addr_lst, send_msg.as_string())
    smtp.quit()
    


def send_email_with_attachment(content, header, file_path,rev_addr_lst,
                               host= Config.DefaultConfig().Email.Domain,
                               username= Config.DefaultConfig().Email.Sender,
                               password= Config.DefaultConfig().Email.Password, 
                               sender_addr= Config.DefaultConfig().Email.Sender ) :
    """
    @author: eason.sun
    @content:邮件发送的主要内容
    @header:邮件发送的头部
    @file_path:附件在本地的路径 
    @username:邮件发件人账号
    @password:邮件发件人账号密码
    @sender_addr:邮件发送时，发件人显示地址
    @rev_addr_lst:收件人列表  
    @return None
    @summary: 用于发送邮件内容，内容只带有一个附件
    """
    smtp = smtplib.SMTP()
    smtp.connect(host)
    smtp.login(username, password)
    
    main_msg = email.MIMEMultipart.MIMEMultipart()
    main_msg["Subject"] = Header(header, "utf-8")
    
    text_msg = email.MIMEText.MIMEText(content, _subtype = "html", _charset = "utf-8")
    main_msg.attach(text_msg)
    
    file_attach = MIMEApplication(open(file_path,'rb').read())
    file_attach.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file_path))
    main_msg.attach(file_attach)
    
    try:
        smtp.sendmail(sender_addr, rev_addr_lst, main_msg.as_string())
    finally:
        smtp.quit()



def send_email_with_attachments(content, header, file_paths,
                                host= Config.DefaultConfig().Email.Domain,
                                username= Config.DefaultConfig().Email.Sender,
                                password= Config.DefaultConfig().Email.Password, 
                                sender_addr= Config.DefaultConfig().Email.Sender,
                                rev_addr_lst=  Config.DefaultConfig().Email.Receiver ) : 
    """
    @author: eason.sun
    @content:邮件发送的主要内容
    @header:邮件发送的头部
    @file_paths:附件列表在本地的路径
    @username:邮件发件人账号
    @password:邮件发件人账号密码
    @sender_addr:邮件发送时，发件人显示地址
    @rev_addr_lst:收件人列表
    
    @return: None
    
    @summary: 用于发送邮件内容，内容带有多个附件
    """
    msg = MIMEMultipart()
    msg["Subject"] = Header(header, "utf-8")
    part = MIMEText(content, _subtype = "html", _charset = "utf-8")
    msg.attach(part)
    # 添加附件
    for file_path in file_paths:
        part = MIMEApplication(open(file_path,'rb').read())
        part["Content-Type"] = 'application/octet-stream;name=”%s”' % Header(os.path.basename(file_path), 'utf-8')
        part["Content-Disposition"] = 'attachment;filename= %s' % Header(os.path.basename(file_path), 'utf-8')
        msg.attach(part)
    try:
        s = smtplib.SMTP(host)
        s.login(username, password)
        s.sendmail(sender_addr, rev_addr_lst, msg.as_string())
    finally:
        s.close()
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import smtplib

from setting.connect_setting import get_email_setting
from logger.logger import get_logger, close_handler

def send_email(title, content):
    logger = get_logger()

    email_setting = get_email_setting()

    #建立MIMEMultipart物件
    email = MIMEMultipart()

    #郵件標題
    email["subject"] = title

    #寄件者
    email["from"] = email_setting['sender']

    #收件者
    email["to"] = email_setting['receiver']

    #郵件內容
    email.attach(MIMEText(content))

    #設定SMTP伺服器
    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  
        try:
            #驗證SMTP伺服器
            smtp.ehlo()  

            #建立加密傳輸
            smtp.starttls()

            #登入寄件者gmail
            smtp.login(email_setting['sender'], email_setting['sender_password'])  

        except smtplib.SMTPException as e:
            logger.error("BaseException : %s" % e, exc_info=True)

        else:
            #寄送郵件
            smtp.send_message(email)

        finally:
            smtp.quit()
            close_handler(logger)
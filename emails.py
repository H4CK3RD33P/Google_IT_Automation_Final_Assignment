#!/usr/bin/env python3
from email.message import EmailMessage
import mimetypes
import os
import smtplib

def generate_email(sender,recipient,subject,body,attachment):
    message = EmailMessage()
    message['From']=sender
    message['To']=recipient
    message['Subject']=subject
    message.set_content(body)
    if attachment!=None:
        attachment_name=os.path.basename(attachment)
        mime_type,_=mimetypes.guess_type(attachment)
        mime_type,mime_subtype=mime_type.split('/')
        with open(attachment,"rb") as file:
            message.add_attachment(file.read(),maintype=mime_type,subtype=mime_subtype,filename=attachment_name)
    return message

def send_email(message):
    mail_server=smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()

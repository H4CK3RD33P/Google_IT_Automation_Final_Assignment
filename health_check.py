#!/usr/bin/env python3
import psutil
import socket
import emails

def check_disk():
    du=psutil.disk_usage('/')
    free_disk_percent=(du.free/du.total)*100
    return (free_disk_percent>20)

def check_memory():
    vm=psutil.virtual_memory()
    available_memory=vm.available//(1024**2)
    return (available_memory>500)

def cpu_check():
    return psutil.cpu_percent(1)>20

def check_localhost():
    return (socket.gethostbyname('localhost')=='127.0.0.1')

if __name__=="__main__":
    sender="automation@example.com"
    recipient="username@example.com"
    body="Please check your system and resolve the issue as soon as possible."
    if not check_disk():
        subject="Error - Available disk space is less than 20%"
        message=emails.generate_email(sender,recipient,subject,body,None)
        emails.send_email(message)
    if not check_memory():
        subject="Error - Available memory is less than 500MB"
        message=emails.generate_email(sender,recipient,subject,body,None)
        emails.send_email(message)
    if not cpu_check():
        subject="Error - CPU usage is over 80%"
        message=emails.generate_email(sender,recipient,subject,body,None)
        emails.send_email(message)
    if not check_localhost():
        subject="Error - localhost cannot be resolved to 127.0.0.1"
        message=emails.generate_email(sender,recipient,subject,body,None)
        emails.send_email(message)
#!/usr/bin/env python3
import run
import reports
from datetime import datetime
import emails

if __name__=="__main__":
    paragraph=run.process_txt()
    title="Processed Update on {}".format(datetime.now().strftime("%B %d, %Y"))
    reports.generate_report("./processed.pdf",title,paragraph)
    sender="automation@example.com"
    recipient="username@example.com"
    subject="Upload Completed - Online Fruit Store"
    body="""All fruits are uploaded to our website successfully. A detailed list is attached to this email."""
    attachment="./processed.pdf"
    message=emails.generate_email(sender,recipient,subject,body,attachment)
    emails.send_email(message)
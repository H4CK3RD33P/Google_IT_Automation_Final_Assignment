#!/usr/bin/env python3
import run
import reports
from datetime import datetime

if __name__=="__main__":
    paragraph=run.process_txt()
    title="Processed Update on {}".format(datetime.now().strftime("%B %d, %Y"))
    reports.generate_report("./processed.pdf",title,paragraph)
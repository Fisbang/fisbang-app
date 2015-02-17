from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from flask import url_for

import smtplib

ADMINS = []

def config(admins = None):
    global ADMINS
    ADMINS = admins

def send_created_project(project_id):

    url = url_for('market.project_details', project_id=project_id)

    text_plain = "There is a new created project http://www.fisbang.com/{}".format(url)

    text_html = "There is a new created project <a href='http://www.fisbang.com{}'>click here</a>".format(url)

    for admin in ADMINS:
        _send_email(admin, 
                    "info@fisbang.com", 
                    subject="New Project!", 
                    text_plain=text_plain,
                    text_html = text_html)
        return True

def _send_email(to, fro, subject="", text_plain="", text_html=""):

    msg = MIMEMultipart('alternative')

    msg['Subject'] 	= subject
    msg['From'] 	= fro
    msg['To'] 		= to

    part1 = MIMEText(text_plain, 'plain')
    part2 = MIMEText(text_html, 'html')
    msg.attach(part1)
    msg.attach(part2)

    s = smtplib.SMTP('localhost')
    s.sendmail(fro, to, msg.as_string())
    s.quit()


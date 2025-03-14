import smtplib

from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Leslie Williams'
email['to'] = 'l.marie1598@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'
email.set_content(
    'I think you are amazing! You are the best person in the world! You have won 1,000,000 dollars! Click here to claim your prize!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('l.marie1598@gmail.com', '')
    smtp.send_message(email)
    print('all good boss!')

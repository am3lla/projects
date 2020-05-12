#!/usr/bin/env python3

from smtplib import SMTP
from email.mime.text import MIMEText

body = "This is my test email, how are you?"

msg = MIMEText(body)
msg["From"] = "email"
msg["To"] = "email"
msg["Subject"] = "Hello"

server = SMTP("smtp.google.com", 587)
server.starttls()
server.login("email", "password")
server.send_message(msg)
print("mail sent")
server.quit()

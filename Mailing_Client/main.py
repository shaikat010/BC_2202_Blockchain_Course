import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# smtp.gmail.com is my smtp server provider
server = smtplib.SMTP('smtp.gmail.com', 25)

# starting the server
server.ehlo()

# try to save the password and email in text file in
# encrypted form
with open('password.txt', 'r') as f:
    password = f.read()

server.login('emp.site2021@gmail.com', password)

# defining the message as a minemultipart
msg = MIMEMultipart()
msg['From'] = 'Shaikat Majumder'
msg['To'] = 'testmail@spaml.de'

msg['Subject'] = "Test Subject"

with open('message.txt', 'r') as f:
    message = f.read()

# this is for adding the message as a plaintext
msg.attach(MIMEText(message, 'plain'))

# now here we re going to attach an image
filename = 'image.jpg'
# rb = reading bite mode
attachment = open(filename, 'rb')

# payload object
P = MIMEBase('application', 'octet-stream')
P.set_payload((attachment.read()))

# Encoding the payload object
encoders.encode_base64(P)
P.add_header("Content-Disposition", f'attachment; filename={filename}')

# adding the payload to the message
msg.attach(P)

text = msg.as_string()
server.sendmail('emp.site2021@gmail.com', 'receiving email', text)

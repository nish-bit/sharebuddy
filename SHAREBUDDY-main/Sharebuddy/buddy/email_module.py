import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

contacts = ['thok732@gmail.com', 'test@example.com']

msg = EmailMessage()
msg['Subject'] = 'A resorce pooling web application!'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'thok732@gmail.com'

msg.set_content('This is a plain text email')

msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">SHAREBUDDY</h1>
    </body>
</html>
""", subtype='html')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login('thok732@gmail.com', 'lucifer9305198393')
    smtp.send_message(msg)
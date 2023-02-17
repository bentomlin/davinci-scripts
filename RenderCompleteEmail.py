# -*- coding: utf-8 -*-

import os
import datetime
import smtplib
from email.mime.text import MIMEText

now = datetime.datetime.now()
time_string = now.strftime("%H:%M:%S %d/%m/%Y")

# Edit here =========================================
recipient_email = 'your.recipient.email.goes.here@gmail.com'

sender_name = 'Your Name Goes Here'
sender_email = 'your.sender.email.goes.here@gmail.com'
sender_password = 'your.sender.email.password'
sender_imap_server = "your.imap.server.address" # mail.mydomain.com
sender_imap_port = 587 # your imap server's port number

message_subject = "Render Complete"
message_body = "Your render completed at "+time_string

# Add a file path to a sound here and remove the # signs from the next two lines to have a sound player when render finishes
# path_to_system_sound = "/Users/yourname/to/a/folder/with/a/sound.aiff"
# os.system('afplay '+path_to_system_sound)


# Don't edit from here down ===========================
sender_fullstring = sender_name+' <'+sender_email+'>'
message = MIMEText(message_body)

message["Subject"] = message_subject
message["From"] = sender_email
message["To"] = recipient_email

try:
    server = smtplib.SMTP(sender_imap_server, sender_imap_port)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_fullstring, recipient_email, message.as_string())
finally:
    server.quit()
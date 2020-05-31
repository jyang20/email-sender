import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path


# Sender info
email = input("Email: ")
password = input("Password: ")

# Message info
subject = 'I, Jessie, demand justice for George Floyd'
msgFile = open("E:\GitHub\email-sender\justice_for_floyd.txt", "r")
message = msgFile.read()

# Send-to emails
send_to_emails = []
# emailsFile = open("E:\GitHub\email-sender\\testEmails.txt", "r")
emailsFile = open("E:\GitHub\email-sender\emails.txt", "r")
for line in emailsFile:
    print(line)
    send_to_emails.append(line)

# Send-to names
send_to_names = []
namesFile = open("E:\GitHub\email-sender\\reps.txt", "r")
name = ''
for line in namesFile:
    for word in line.split():
        name += word
        name += ' '
    length = len(name) - 1
    trunc_name = name[:length]
    send_to_names.append(trunc_name)
    name = ''

# Connect and login to the email server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)

# Loop over each email to send to
for i,send_to_email in enumerate(send_to_emails):
    # Setup MIMEMultipart for each email address (if we don't do this, the emails will concat on each email sent)
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = send_to_email
    msg['Subject'] = subject

    ###### This is where we can edit the message is needed ######
    perMsg = 'Dear Representative ' + send_to_names[i] + ',\n' + message

    # Attach the message to the MIMEMultipart object
    msg.attach(MIMEText(perMsg, 'plain'))

    # Send the email to this specific email address
    server.sendmail(email, send_to_email, msg.as_string())

# Quit the email server when everything is done
server.quit()

# Project 1 - Auto Email Sender

# Step 1: import python library to be used
import smtplib # send email
import ssl # 建立安全加密的 connection
from email.message import EmailMessage # create email template

# Step 2: creat a function to send email
def email_sender(sender_email, app_password, recipient_email, subject, message):
  # Step 2.1: create a email
  msg = EmailMessage() # activate library to create email
  msg['From'] = sender_email
  msg['To'] = recipient_email
  msg['Subject'] = subject
  msg.set_content(message)

  # Step 2.2: setup secure connection with server
  connection = ssl.create_default_context()
  with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    server.login(sender_email, app_password)
    server.send_message(msg)
    print('Email sent successfully!')

# Step 3: Provide specific information (using input())
sender_email = 'example1.codegen@gmail.com'
app_password = 'nbujmcnefkjsafyu'
recipient_email = input('Enter your email address: ')
subject = input('Subject: ')
message = input('Message Content: ')

# Step 4: Activate send_email()
email_sender(sender_email, app_password, recipient_email, subject, message)

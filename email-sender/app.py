from email.message import EmailMessage
import smtplib, ssl

email_sender = ""
password = ""

email_receiver = ""
subject = "Hello"
body = """
Please signup my page
"""
em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["subject"] = subject
em.set_content(body)

context= ssl.create_default_context()

 

server = smtplib.SMTP_SSL('smtp.gmail.com:465')
server.login(email_sender, password)

try:
    # Attempt to send an email
    server.sendmail(email_sender, email_receiver, em.as_string())
except smtplib.SMTPException as e:
    print(f"SMTP error occurred: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

print('Sent')
server.quit()

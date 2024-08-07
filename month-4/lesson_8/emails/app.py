import smtplib
import threading
import random

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_sender = 'sanjarbekwork@gmail.com'
smtp_password = 'nlcg jpcd umyu zcog'


def send_mail(to_user, subject, message):
    email = f"Subject: {subject}\n\n{message}"
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_sender, smtp_password)
        server.sendmail(smtp_sender, to_user, email)
        server.quit()
    except smtplib.SMTPException as e:
        print(f"Failed {e}")


user_email = input("To user: ")
user_subject = input("Subject: ")
user_message = input("Message: ")

t = threading.Thread(target=send_mail, args=(user_email, user_subject, user_message,))
t.start()
print("Email is sent")







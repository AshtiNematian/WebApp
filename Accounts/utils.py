from django.core.mail import EmailMessage

import threading


class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data['email_subject'], from_email='Ashtinematian1@gmail.com', body=data['email_body'],
            to=[data['to_email']])
        EmailThread(email).start()

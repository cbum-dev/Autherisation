from django.core.mail import send_mail
from django.conf import settings

def send_email_to_client():
    subject = "Hi boys"
    message = "Email sent LOL"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["priyanshukumar20022304@gmail.com"]
    send_mail(subject,message,from_email,recipient_list)



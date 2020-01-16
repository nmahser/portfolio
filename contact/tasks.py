from celery import shared_task

from django.core.mail import send_mail


@shared_task
def sendEmailTask(subject, message, from_email):

    try:
        sendEmail = send_mail(subject, from_email + " " + message, "nmahser@yandex.com",
                              ["nmahser@mail.usf.edu"])

    # In case if an e-mail fail we can at least see the sender. This is just better than nothing...
    except Exception:
        sendEmail = "email failed. sender: " + from_email

    return sendEmail

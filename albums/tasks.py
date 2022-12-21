from celery import shared_task
from django.core.mail import send_mail
from time import sleep

@shared_task
def send_congratulation_email(artist,album):    
    print('hommos')
    sleep(5)
    send_mail(
        subject="Congrats",
        message=f"Hello {artist['username']} , Your album {album['name']} has been created successfully.",
        from_email="settings.EMAIL_HOST_USER",
        recipient_list=[artist['email']],
        fail_silently=True
    )
    return "Sent!"
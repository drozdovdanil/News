from allauth.account.signals import user_signed_up
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string

from .models import PostCategory, User


def send_notification(preview, pk, title, subscribers):
    html_content = render_to_string(
        'post_created_email.html',
        {'text': preview,
         'link': f'{settings.SITE_URL}/{pk}'}
    )

    msg = EmailMultiAlternatives(
        subject=title,
        body="",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.category.all()
        subscribers: list[str] = []
        for category in categories:
            subscribers += category.subscribers.all()

        subscribers = [s.email for s in subscribers]

        send_notification(instance.preview(), instance.pk, instance.title, subscribers)


# def send_welcome_email():
#     print('hi')
#     msg = EmailMultiAlternatives(
#         subject="Добро рожаловать",
#         body="Добро рожаловать",
#         from_email=settings.DEFAULT_FROM_EMAIL,
#         to=user_email,
#     )
#
#     msg.send()
#
#
# @receiver(user_signed_up)
# def welcome_email(sender, **kwargs):
#     send_welcome_email()
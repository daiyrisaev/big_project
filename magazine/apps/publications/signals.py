from django.core.mail import send_mail, send_mass_mail
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from .models import Publication
from django.conf import settings

# @receiver(post_save,sender=Publication)
# def publication_handler(sender, instance, created, **kwargs):
#     if created:
#         print(f'Создалось Публикация')
#
#         send_mail(
#             subject='обнавилось публикация.',
#             message=Publication.objects.get('title'),
#             from_email=settings.EMAIL_HOST_USER,
#             recipient_list=['isaevdaiyr@gmail.com'],

    #     )
    # else:
    #     print('Публикация Обновилась')
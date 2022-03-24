from django.conf import settings
from django.contrib import admin
from django.core.mail import send_mail

from apps.publications.models import Publication, PublicationCategory, UserMail


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    pass

    def save_model(self,request,obj,form,change):
         print(f'{request=}')
         print(f'{obj=}')
         print(f'{form=}')
         print(f'{change=}')
         if not change:
             try:
                 send_mail(
                      subject='Создалось публикация.',
                      message='создалось публикация.',
                      from_email=settings.EMAIL_HOST_USER,
                      recipient_list=['isaevdaiyr@gmail.com'],

         )
             except Exception as exc:
              print(exc)
         # request=PublicationCategory.title
         # if send_mail(
         #         message=PublicationCategory.title,
         #         subject=PublicationCategory.title,
         #         from_email=settings.EMAIL_HOST_USER,
         #         recipient_list=['isaevdaiyr@gmail.com']):
         #     # print(request)
         return super(PublicationAdmin,self).save_model(request,obj,form,change)


@admin.register(PublicationCategory)
class PublicationCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(UserMail)
class UserMailAdmin(admin.ModelAdmin):
    pass


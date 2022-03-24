from django.db import models


class PublicationCategory(models.Model):
    title = models.CharField(max_length=200,unique=True)

    class Meta:
        verbose_name='категория'
        verbose_name_plural='категории'

    def __str__(self):
       return   self.title


class Publication(models.Model):
    category = models.ForeignKey(to=PublicationCategory,null=True,on_delete=models.SET_NULL,related_name='publication_set')
    title = models.CharField(max_length=150)
    description = models.TextField()
    poster = models.ImageField(upload_to='publication_images')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name ='публикация'
        verbose_name_plural ='публикации'

    def __str__(self):
        return self.title


class UserMail(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользаватели'


    def __str__(self):
        return self.name


# class MyPublication(models.Model):
#     title = models.CharField(max_length=150)
#     description = models.TextField()
#     poster = models.ImageField(upload_to='publication_images')
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         verbose_name = 'публикация'
#         verbose_name_plural = 'публикациии'
#
#
#     def __str__(self):
#         return self.title

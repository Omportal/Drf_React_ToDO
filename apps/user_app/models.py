from django.db import models

# Create your models here.


class CustomUser(models.Model):
    username = models.CharField(max_length=64, verbose_name="Никнэйм")
    firstname = models.CharField(max_length=64, verbose_name="Имя")
    lastname = models.CharField(max_length=64, verbose_name="Фамилия")
    email = models.EmailField(unique=True, verbose_name="Почта")

    class Meta:
        verbose_name = 'Юзер'
        verbose_name_plural = 'Юзеры'
    
    def __str__(self):
        return self.username
    
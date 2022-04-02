from django.contrib.auth.models import AbstractUser
from django.db import models


class UserDRF(AbstractUser):
    email = models.EmailField(verbose_name='e-mail', unique=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-pk']

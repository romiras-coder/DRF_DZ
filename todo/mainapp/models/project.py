from django.db import models
from authapp.models.users import UserDRF


class Project(models.Model):
    name = models.CharField(verbose_name='Название проекта', blank=False, max_length=255)
    users = models.ManyToManyField(UserDRF, verbose_name='Пользователи проекта')
    link = models.URLField(verbose_name='Ссылка на репозиторий', blank=True, null=True)
    user_created = models.ForeignKey(UserDRF, verbose_name='Пользователь, создавший проект', on_delete=models.CASCADE,
                             related_name='userdrf', blank=True, null=True)
    date_create = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проект'
        ordering = ['-date_create']

    def __str__(self):
        return f"{self.pk}"

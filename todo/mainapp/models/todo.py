from django.db import models
from authapp.models.users import UserDRF
from .project import Project


class Todo(models.Model):
    text = models.TextField(verbose_name='Описание', blank=False)
    user_created = models.ForeignKey(UserDRF, verbose_name='Пользователь, создавший заметку', on_delete=models.CASCADE,
                                     related_name='todo_user_created', blank=True, null=True)
    project = models.ForeignKey(Project, verbose_name='Проект', on_delete=models.CASCADE, blank=True, null=True)
    statuses = (
        ('активно', 'активно'),
        ('закрыто', 'закрыто')
    )
    status = models.CharField(verbose_name='Статус', max_length=20, choices=statuses, blank=True, default='активно')
    date_create = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True, null=True)
    date_update = models.DateTimeField(verbose_name='Дата изменения', auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметка'
        ordering = ['-date_create']

    def __str__(self):
        return f"{self.pk}"

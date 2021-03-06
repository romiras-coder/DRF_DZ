# Generated by Django 2.2.16 on 2022-04-12 21:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название проекта')),
                ('date_create', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_user', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь, создавший проект')),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Пользователи проекта')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проект',
                'ordering': ['-date_create'],
            },
        ),
    ]

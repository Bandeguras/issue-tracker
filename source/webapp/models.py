from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


# Create your models here.
class Task(models.Model):
    summary = models.CharField(max_length=30, verbose_name="Заголовок")
    description = models.TextField(max_length=3000, verbose_name="Описание", null=True, blank=True)
    status = models.ForeignKey('webapp.Status', on_delete=models.PROTECT, related_name='statuses')
    type = models.ManyToManyField('webapp.Type', related_name='types')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата начала")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата окончания")
    project = models.ForeignKey('webapp.Project', on_delete=models.CASCADE, related_name='projects')
    likes = models.ManyToManyField(get_user_model(), related_name='tasks_likes', verbose_name='Лайки')

    def get_absolute_url(self):
        return reverse('webapp:task', kwargs={'pk': self.pk})


class Type(models.Model):
    name = models.CharField(max_length=30, verbose_name="Типы")

    def __str__(self):
        return f'{self.name}'


class Status(models.Model):
    name = models.CharField(max_length=30, verbose_name="Статус")

    def __str__(self):
        return f'{self.name}'


class Project(models.Model):
    author = models.ManyToManyField(get_user_model(), default=1, related_name='projects', verbose_name='Автор')
    created_at = models.DateField(verbose_name="Время создания")
    expiration_at = models.DateField(verbose_name="Время изменения", null=True, blank=True)
    summary = models.CharField(max_length=30, verbose_name="Заголовок")
    description = models.TextField(max_length=3000, verbose_name="Описание")
    likes = models.ManyToManyField(get_user_model(), related_name='projects_likes', verbose_name='Лайки')

    def get_absolute_url(self):
        return reverse('webapp:project', kwargs={'pk': self.pk})

    class Meta:
        permissions = [('add_user_in_project', 'Добавить пользователя в проект'), ]

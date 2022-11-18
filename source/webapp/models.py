from django.db import models

TYPES_CHOICES = [('Task', 'задача'), ('Bug', 'ошибка'), ('Enhancement', 'улучшение')]
CATEGORY_CHOICES = [('New', 'новый'), ('In Progress', 'в процессе'), ('Done', 'выполнено')]


# Create your models here.
class Task(models.Model):
    summary = models.CharField(max_length=30, verbose_name="Заголовок")
    description = models.TextField(max_length=3000, verbose_name="Описание", null=True, blank=True)
    status = models.ForeignKey('webapp.Status', on_delete=models.PROTECT, related_name='statuses')
    type = models.ForeignKey('webapp.Type', on_delete=models.PROTECT, related_name='types')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время изменения")


class Type(models.Model):
    name = models.CharField(max_length=30, choices=TYPES_CHOICES, verbose_name="Типы")

    def __str__(self):
        return f'{self.name}'


class Status(models.Model):
    name = models.CharField(max_length=30, choices=CATEGORY_CHOICES, verbose_name="Статус")

    def __str__(self):
        return f'{self.name}'

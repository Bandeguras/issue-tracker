# Generated by Django 4.1.3 on 2023-01-03 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0012_remove_task_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'permissions': [('add_user_in_project', 'Добавить пользователя в проект')]},
        ),
    ]
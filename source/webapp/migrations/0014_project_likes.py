# Generated by Django 4.1.3 on 2023-01-29 15:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0013_alter_project_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='likes',
            field=models.ManyToManyField(related_name='projects_likes', to=settings.AUTH_USER_MODEL, verbose_name='Лайки'),
        ),
    ]

from django.db import models
from django.contrib.auth import get_user_model


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), related_name='profile', on_delete=models.CASCADE, verbose_name='Пользователь')
    avatar = models.ImageField(blank=True, null=True, upload_to='user_avatar', verbose_name="Аватар")
    git = models.URLField(blank=True, null=True, max_length=256, verbose_name="ГитХаб")
    description = models.TextField(blank=True, null=True, max_length=3000, verbose_name="О себе")

    def __str__(self):
        return f"{self.user.get_full_name()} 's Profile "

    class Meta:
        db_table = 'profile'
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

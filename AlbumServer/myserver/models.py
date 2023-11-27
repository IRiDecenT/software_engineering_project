from django.db import models
from AlbumServer.settings import BASE_URL
# Create your models here.

# 用户表
class User(models.Model):
    username = models.CharField(max_length=32, verbose_name='用户名', unique=True, null=False, default='default')
    password = models.CharField(max_length=64, verbose_name='密码', null=False)
    avatar = models.CharField(max_length=256, verbose_name='头像', null=False,
                              default=BASE_URL + 'static/avatar/defaultAvatar.jpg')

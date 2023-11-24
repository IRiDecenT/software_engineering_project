from django.db import models

# Create your models here.

# 用户表
class User(models.Model):
    username = models.CharField(max_length=100, verbose_name='用户名', unique=True, null=False, default='default')
    password = models.CharField(max_length=100, verbose_name='密码', null=False, default='default')

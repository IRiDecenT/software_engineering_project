from django.db import models
from AlbumServer.settings import BASE_URL
# Create your models here.

# 用户表
class User(models.Model):
    username = models.CharField(max_length=32, verbose_name='用户名', unique=True, null=False, default='default')
    password = models.CharField(max_length=64, verbose_name='密码', null=False)
    avatar = models.CharField(max_length=256, verbose_name='头像', null=False,
                              default=BASE_URL + '/static/avatar/defaultAvatar.jpg')


class Album(models.Model):
    name = models.CharField(max_length=32, verbose_name='相册名', null=False)
    discription = models.CharField(max_length=1024, verbose_name='相册描述', null=False, default="这个人很懒，什么都没有留下")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

class Photo(models.Model):
    name = models.CharField(max_length=32, verbose_name='图片名', null=False)
    discription = models.CharField(max_length=1024, verbose_name='图片描述', null=False, default="这个人很懒，什么都没有留下")
    upload_time = models.DateTimeField(auto_now_add=True, verbose_name='上传时间')
    url = models.CharField(max_length=256, verbose_name='图片url地址', null=False)

class PhotoAlbum(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, verbose_name='图片')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, verbose_name='相册')

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, verbose_name='图片')
    content = models.CharField(max_length=1024, verbose_name='评论内容', null=False)
    comment_time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')

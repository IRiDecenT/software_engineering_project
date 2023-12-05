from django.shortcuts import render
from django.http import JsonResponse
import myserver.models as models
import json
from AlbumServer.settings import SYSTEM_PATH, BASE_URL
from myserver.util.auxiliaryFunc import check_and_delete
# Create your views here.


def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        print(username, password)
        try:
            user = models.User.objects.get(username=username)
            if user.password == password:
                ret = {
                    'code': 200,
                    'msg': '登录成功',
                    'id': user.id,
                }
                return JsonResponse(ret)
            else:
                return JsonResponse({'code': 400, 'msg': '密码错误'})
        except:
            return JsonResponse({'code': 400, 'msg': '用户不存在'})
    else:
        return JsonResponse({'code': 400, 'msg': '请求方式错误'})


def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        print(username, password)
        try:
            user = models.User.objects.get(username=username)
            return JsonResponse({'code': 400, 'msg': '用户已存在'})
        except:
            user = models.User(username=username, password=password)
            user.save()
            return JsonResponse({'code': 200, 'msg': '注册成功'})
    else:
        return JsonResponse({'code': 400, 'msg': '请求方式错误'})

# get请求没有body，所以要用url传参
def get_UserInfo(request, id):
    if request.method == 'GET':
        try:
            user = models.User.objects.get(id=id)
            # 通过userid获取xx用户的相册信息
            # 把用户信息和相册信息返回
            ret = {
                'code': 200,
                'msg': '获取成功',
                'username': user.username,
                'avatar': user.avatar,
            }
            return JsonResponse(ret)
        except:
            return JsonResponse({'code': 400, 'msg': '用户不存在'})
    else:
        return JsonResponse({'code': 400, 'msg': '请求方式错误'})

def createAlbum(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data['name']
        discription = data['discription']
        user_id = data['uid']
        print(name, discription, user_id)
        try:
            user = models.User.objects.get(id=user_id)
            album = models.Album(name=name, discription=discription, user=user)
            album.save()
            return JsonResponse({'code': 200, 'msg': '创建成功'})
        except:
            return JsonResponse({'code': 400, 'msg': '用户不存在'})
    else:
        return JsonResponse({'code': 400, 'msg': '请求方式错误'})

def getAlbums(request, id):
    if request.method == 'GET':
        try:
            user = models.User.objects.get(id = id)
            print(user.username)
            # 通过userid获取xx用户的相册信息
            all_album = models.Album.objects.filter(user=user)
            album_list = []
            for album in all_album:
                album_list.append({
                    'id': album.id,
                    'name': album.name,
                    'discription': album.discription,
                    'create_time': album.create_time,
                    'forePage': album.forePage
                })
                # JsonResponse只能返回字典，所以要把album_list设置成safe=False
            return JsonResponse(album_list, safe=False)
        except Exception as e:
            print(type(e), e)
            return JsonResponse({'code': 400, 'msg': '用户不存在'})
    else:
        return JsonResponse({'code': 400, 'msg': '请求方式错误'})

# 前端发起一个post请求，表单类型，包含头像图片文件以及用户id
def updateAvator(request):
    if request.method == 'POST':
        try:
            avatar = request.FILES['avatar']
            uid = request.POST['uid']
            print(avatar.name, avatar.size, uid)
            # 文件保存到本地， 用户id-相册id-文件名 例如 1-1-avatar1.jpg， 方便日后查找删除
            file_name = str(uid) + '-' + avatar.name
            file_path = SYSTEM_PATH + 'avatars/' + file_name
            check_and_delete(id=uid, mainPath=SYSTEM_PATH + 'avatars/')
            # 打开一个二进制文件，写入文件
            with open(file_path, 'wb') as f:
                for chunk in avatar.chunks():
                    f.write(chunk)
            # 更新数据库
            user = models.User.objects.get(id=uid)
            user.avatar = BASE_URL + '/static/avatars/' + file_name
            user.save()
            result = {
                'code': 200,
                'msg': '更新成功',
                'filename': avatar.name,
                'avatar': user.avatar
            }
            return JsonResponse(result, status=200)
        except Exception as e:
            print(type(e), e)
            return JsonResponse({'code': 400, 'msg': '更新失败'})


def uploadPhotos(request):
    if request.method == 'POST':
        try:
            uid = request.POST['uid']
            aid = request.POST['aid']
            photos = request.FILES.getlist('photos')
            print(uid, aid)
            for photo in photos:
                print(photo.name, photo.size)
            # 文件保存到本地， 用户id-相册id-文件名 例如 1-1-image1.jpg， 方便日后查找删除
            for photo in photos:
                file_name = str(uid) + '-' + str(aid) + '-' + photo.name
                file_path = SYSTEM_PATH + 'images/' + file_name
                # 打开一个二进制文件，写入文件
                with open(file_path, 'wb') as f:
                    for chunk in photo.chunks():
                        f.write(chunk)
                # 更新数据库
                # user = models.User.objects.get(id=uid)
                album = models.Album.objects.get(id=aid)
                photo = models.Photo(name=photo.name, url=BASE_URL + '/static/images/' + file_name)
                photo.save()
                photo_album = models.PhotoAlbum(photo=photo, album=album)
                photo_album.save()
            result = {
                'code': 200,
                'msg': '上传成功',
            }
            return JsonResponse(result, status=200)
        except Exception as e:
            print(type(e), e)
            return JsonResponse({'code': 400, 'msg': '上传失败'})

def getPhotos(request, aid):
    if request.method == 'GET':
        try:
            album = models.Album.objects.get(id=aid)
            print(album.name)
            photo_album_list = models.PhotoAlbum.objects.filter(album=album)
            photos = [ photo_album.photo for photo_album in photo_album_list ]
            photo_list = []
            for photo in photos:
                photo_list.append({
                    'id': photo.id,
                    'name': photo.name,
                    'discription': photo.discription,
                    'upload_time': photo.upload_time,
                    'url': photo.url
                })
            print(photo_list)
            return JsonResponse(photo_list, safe=False)
        except Exception as e:
            print(type(e), e)
            return JsonResponse({'code': 400, 'msg': '相册不存在'})
    else:
        return JsonResponse({'code': 400, 'msg': '请求方式错误'})
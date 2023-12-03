from django.shortcuts import render
from django.http import JsonResponse
import myserver.models as models
import json
# Create your views here.


def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        print(username, password)
        try:
            user = models.User.objects.get(username=username)
            print(user.username, user.password)
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
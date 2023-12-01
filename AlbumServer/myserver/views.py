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


def get_UserInfo(request):
    if request.method == 'GET':
        data = json.loads(request.body)
        id = data['id']
        print(id)
        try:
            user = models.User.objects.get(id=id)
            ret = {
                'code': 200,
                'msg': '获取成功',
                'username': user.username,
                'avator': user.avatar
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
from django.shortcuts import render
from django.http import JsonResponse
import myserver.models as models
import json
# Create your views here.


#requst.POST是类似字典类型对象，可以通过get方法获取键值对
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        print(username, password)
        try:
            user = models.User.objects.get(username=username)
            if user.password == password:
                return JsonResponse({'code': 200, 'msg': '登录成功'})
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


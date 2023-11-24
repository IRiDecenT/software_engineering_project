from django.shortcuts import render
from django.http import JsonResponse
import myserver.models as models
# Create your views here.



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
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


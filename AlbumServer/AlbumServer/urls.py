"""
URL configuration for AlbumServer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myserver.views import login, register, get_UserInfo
from django.conf.urls.static import static
from django.conf import settings


# http://127.0.0.1:8000/static/avatars/defaultAvatar.jpg 可以访问到django的静态文件
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login),
    path('register/', register),
    path('getUserInfo/', get_UserInfo),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

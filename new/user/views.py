from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import authenticate
from django.contrib import auth
from .models import Myuser

def registerView(request):
    button_right='登录'
    url = '/login/'
    register =  True
    if request.method=='GET':
        return render(request,'user.html',locals())

    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        is_active= request.POST.get('is_active')
        if Myuser.objects.filter(username=username,password=password):
            tips = '用户已存在，请重新注册'
            return render(request,'user.html',locals())
        else:
            #创建django user系统中的user，并将密码以加密形式写入数据库
            user=Myuser.objects.create_user(
                username=username,
                password=password,
                mobile=mobile,
                email=email,
                is_active=1)
            user.save()
            tips = '注册成功，请登录'
            return render(request,'user.html',locals())

class UserBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user=Myuser.objects.get(Q(username=username) | Q(email=username)| Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception :
            return None

def loginView(request):
    button_right = '注册'
    url='/register/'
    login = True
    if request.method == 'GET':
        return render(request,'user.html',locals())
    else:
        username =request.POST.get('username')
        password=request.POST.get('password')
        if Myuser.objects.filter(username=username):
            user = authenticate(username=username,password=password)
            if user:
                auth.login(request,user)
                tips='登录成功'
                return render(request,'user.html',locals())
            else:
                tips='密码错误，请重新输入'
                return render(request, 'user.html', locals())
        else:
            tips='用户不存在，请注册'
            return render(request, 'user.html', locals())
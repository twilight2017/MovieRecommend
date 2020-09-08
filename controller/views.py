import socket

from django.shortcuts import render
from .models import Users
from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth import login as LOGIN
from django.contrib.auth import logout as LOGOUT
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
import os
from controller import test
from controller.OpenCV_Motion import main
import webbrowser

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

# Users login


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST" and request.POST:
        _username = request.POST.get('username')
        _password = request.POST.get('password')
        # 校验用户
        user = Users.objects.filter(user_name=_username,user_password=_password)
        print(user)
        if user:
            us = Users.objects.get(user_name=_username)
            request.session['name'] = us.user_name
            return redirect('/choose/')
        else:
            return render(request, 'login.html', {'error': '用户名或密码错误！'})
    return render(request, 'login.html')

# new Users register


def register(request):
    result = ''
    if request.method == "POST" and request.POST:
        #  判断是否为POST请求
        u_name = request.POST.get('username')
        u_gender = request.POST.get('gender')
        u_birth = request.POST.get('birthday')
        u_password = request.POST.get('password')
        u_repass = request.POST.get('repassword')
        if u_password == u_repass:
            db = Users.objects.filter(user_name=u_name)
            if db:
                # 该用户已注册过
                result = 'had'
                return render(request, 'register.html', {'result':result})
            else:
                # 注册新用户
                info = Users()
                info.user_name = u_name
                info.user_sex = u_gender
                info.user_id = u_name
                info.user_birth = u_birth
                info.user_password = u_password
                info.save()
                result = 'success'
                request.session['id']=info.user_name
                return render(request, 'register_choose.html', {'result': result})
        else:
            # 两次输入密码不一致
            result = 'error'
            return render(request, 'register.html', {'result':result})
    return render(request, 'register.html')

# choose the movies that you favors


def choose(request):
    if request.method == 'GET':
        return render(request, 'filerecommend.html')
    elif request.method == 'POST' and request.POST:
        u_id = request.session.get('id')
        favor = request.POST.getlist('favor_movie')
        favor = list(map(str, favor))
        Users.objects.filter(user_name=u_id).update(favor_movie = favor)
        return render(request, 'filerecommend.html')
    return render(request, 'register_choose.html')


#  搜索电影
def openbrowser(text):
    maps = {
        '百度': ['百度', 'baidu'],
        '腾讯': ['腾讯', 'tengxun'],
        '网易': ['网易', 'wangyi']

    }
    if text in maps['百度']:
        webbrowser.open_new_tab('https://www.baidu.com')
    elif text in maps['腾讯']:
        webbrowser.open_new_tab('https://www.qq.com')
    elif text in maps['网易']:
        webbrowser.open_new_tab('https://www.163.com/')
    else:
        webbrowser.open_new_tab('https://www.baidu.com/s?wd=%s' % text)


def search(request):
    if request.method == 'POST' and 'yuyin' in request.POST:
        os.system('D:\study\ProDesign\dist\yuyin.exe ')
        return render(request, 'filerecommend.html')
    elif request.method == 'POST' and 'motion' in request.POST:
        main.main
        return render(request, 'filerecommend.html')
    elif request.method == 'POST' and 'search' in request.POST:
        cont = request._post.get('content')
        openbrowser(cont)
    elif request.method == 'POST':
        u_id = request.session.get('id')
        user = Users.objects.get(user_name=u_id)
        reference = user.favor_movie[0]
        listRes = test.recommend('Godfather')
        request.close()
        return render(request, 'filerecommend.html', {'film_list': listRes})
    return render(request, 'filerecommend.html')
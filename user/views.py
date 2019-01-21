from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from user.forms import RegisterForm, LoginForm
from user.models import User


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    if request.method == 'POST':
        # 使用表单form做校验
        form = RegisterForm(request.POST)
        if form.is_valid():
            # 账号不存在与数据库，密码和确认密码一致，邮箱格式正确
            username = form.cleaned_data['username']
            password = make_password(form.cleaned_data['userpwd'])
            User.objects.create(username=username,
                                password=password
                                )
            return HttpResponseRedirect(reverse('user:login'))
        else:
            # 获取表单校验不通过的错误信息
            errors = form.errors
            return render(request, 'register.html', {'errors': errors})


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # 用户名存在，密码相同
            username = form.cleaned_data['username']
            user = User.objects.filter(username=username).first()
            request.session['user_id'] = user.id
            return HttpResponseRedirect(reverse('article:article'))
        else:
            errors = form.errors
            return render(request, 'login.html', {'errors': errors})


def logout(request):
    if request.method == 'GET':
        del request.session['user_id']
        return HttpResponseRedirect(reverse('user:login'))


def manage_user(request):
    if request.method == 'GET':
        activate = 'user'
        return render(request, 'manage-user.html', {'activate':activate})


def loginlog(request):
    if request.method == 'GET':
        activate = 'user'
        return render(request, 'loginlog.html', {'activate':activate})
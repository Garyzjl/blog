"""__author__ - Gary"""

from django import forms
from django.contrib.auth.hashers import check_password

from user.models import User


class RegisterForm(forms.Form):

    username = forms.CharField(max_length=20, min_length=2, required=True,
                               error_messages={
                                    'required': '用户名必填',
                                    'max_length': '用户名不能超过20字符',
                                    'min_length': '用户名不能短于2字符'
                                })
    userpwd = forms.CharField(required=True, max_length=20, min_length=1,
                              error_messages={
                                    'required': '密码必填',
                                    'max_length': '用户名不能超过20字符',
                                    'min_length': '用户名不能短于1字符'
                          })
    reuserpwd = forms.CharField(required=True,
                                max_length=20,
                                min_length=1,
                                error_messages={
                                    'required': '密码必填',
                                    'max_length': '用户名不能超过20字符',
                                    'min_length': '用户名不能短于1字符'
                          })

    def clean_user_name(self):
        # 校验注册的账号是否已存在
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).first()
        if user:
            raise forms.ValidationError('该账号已存在，请更改账号再注册')
        return self.cleaned_data['username']

    def clean(self):
        pwd = self.cleaned_data.get('userpwd')
        cpwd = self.cleaned_data.get('reuserpwd')
        if pwd != cpwd:
            raise forms.ValidationError({'userpwd': '两次密码不一致'})
        return self.cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=2, required=True,
                               error_messages={
                                    'required': '用户名必填',
                                    'max_length': '用户名不能超过20字符',
                                    'min_length': '用户名不能短于2字符'
                                })

    userpwd = forms.CharField(required=True, max_length=20, min_length=1,
                              error_messages={
                                    'required': '密码必填',
                                    'max_length': '用户名不能超过20字符',
                                    'min_length': '用户名不能短于1字符'
                          })

    def clean(self):
        # 校验用户名是否已注册
        username = self.cleaned_data.get('username')
        user = User.objects.filter(username=username).first()
        if not user:
            raise forms.ValidationError({'username': '该用户名未注册'})
        # 校验密码
        password = self.cleaned_data.get('userpwd')
        if not check_password(password, user.password):
            raise forms.ValidationError({'userpwd': '密码错误'})
        return self.cleaned_data


class ColumnForm(forms.Form):
    name = forms.CharField(max_length=10, min_length=2,
                           error_messages={
                               'required': '栏目名称必填',
                               'max_length': '名称不能超过10字符',
                               'min_length': '名称不能少于2字符'
                           })

    alias = forms.CharField(max_length=10, min_length=2,
                            error_messages={
                               'required': '栏目别名必填',
                               'max_length': '名称不能超过10字符',
                               'min_length': '名称不能少于2字符'
                           })



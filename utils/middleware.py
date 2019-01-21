"""__author__ - Gary"""
import re

from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse
from django.http import HttpResponseRedirect

from user.models import User


class LoginMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # 拦截请求之前进行登录状态的校验
        # 1.给request.user属性赋值，赋值为当前用户
        user_id = request.session.get('user_id')
        if user_id:
            user = User.objects.filter(pk=user_id).first()
            request.user = user
        # 2.区分登录校验
        path = request.path
        if path == '/':
            return None
        # 不需要做登录校验的地址
        not_need_check = ['/user/register/', '/user/login/']
        for check_path in not_need_check:
            if re.match(check_path, path):
                # 当前path路径不需要做登录校验的路由
                return None
        # path为需要做登录校验的路由时，判断用户是否登录，没有登录跳转登录页面
        if not user_id:
            return HttpResponseRedirect(reverse('user:login'))










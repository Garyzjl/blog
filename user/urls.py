"""__author__ - Gary"""
from django.urls import path
from user import views

urlpatterns = [
    # 注册
    path('register/', views.register, name='register'),
    # 登录
    path('login/', views.login, name='login'),
    # 退出登录
    path('logout/', views.logout, name='logout'),
    # 管理用户
    path('manage_user/', views.manage_user, name='manage_user'),
    # 管理登录日志
    path('loginlog/', views.loginlog, name='loginlog'),
]
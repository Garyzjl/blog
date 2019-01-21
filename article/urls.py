"""__author__ - Gary"""
from django.urls import path

from article import views

urlpatterns = [
    # 文章管理页面
    path('article/', views.article, name='article'),
    # 添加文章
    path('add_article/', views.add_article, name='add_article'),

]

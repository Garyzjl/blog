"""__author__ - Gary"""
from django.urls import path

from column import views

urlpatterns = [
    # 栏目
    path('category/', views.category, name='category'),
    # 删除栏目
    path('del_col/', views.del_col, name='del_col'),
    #修改栏目
    path('change_col/', views.change_col, name='change_col'),
]
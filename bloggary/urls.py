"""bloggary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from django.contrib.staticfiles.urls import static

from bloggary.settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    # 导入应用
    path('user/', include(('user.urls', 'user'), namespace='user')),
    path('article/', include(('article.urls', 'article'), namespace='article')),
    path('column/', include(('column.urls', 'column'), namespace='column')),
]

# 配置解析Midea文件信息
# from django.contrib.staticfiles.urls import static
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
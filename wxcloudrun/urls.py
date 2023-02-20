"""wxcloudrun URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from wxcloudrun import views
from django.conf.urls import url
from django.urls import path

urlpatterns = (
    # 计数器接口
    url(r'^^api/count(/)?$', views.counter),
    # url(r'^ai(/)?$', views.ai),
    path('ai/', views.ai, name='ai'),
    path('ll',views.ll),
    path('chat',views.chat)
    # 获取主页
    # url(r'(/)?$', views.index),
)

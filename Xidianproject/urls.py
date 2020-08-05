"""Xidianproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from xdweb.views import homepage,showpost,showpost1,showpost2,showpost3,showpost4,showpost5,showpost6,showpost7,showpost8

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage),
    path('post/', showpost),
    path('post1/', showpost1),
    path('post2/', showpost2),
    path('post3/', showpost3),
    path('post4/', showpost4),
    path('post5/', showpost5),
    path('post6/', showpost6),
    path('post7/', showpost7),
    path('post8/', showpost8),
]

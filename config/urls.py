"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, re_path, include

from accounts import views as accounts_views
from shop import views as shop_views
from . import views

urlpatterns = [
    re_path(r'^admin/$', admin.site.urls),
    re_path(r'^$', views.index),
    re_path(r'^accounts/$', include('acounts.urls')),
    re_path(r'^shop/$', include('shop.urls')),
    re_path(r'^shop/(?P<book_id>\d+)/$', shop_views.detail, name='shop_detail')
]

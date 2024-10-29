from django.urls import re_path

from . import views

app_name = "accounts"

urlpatterns = [
    re_path(r'^login/$', views.login, name='login'),
    re_path(r'^logout/$', views.logout, name='logout'),
    re_path(r'^register/$', views.register, name="register"),
]

# -*- coding: utf-8 -*-
from . import views
from django.urls import path
urlpatterns=[
        path('index',views.index,name="index"),
        path('register', views.sign_up, name='register'),
        path('login', views.sign_in, name='login'),
        path('logout1', views.log_out, name='logout1'),
    ]

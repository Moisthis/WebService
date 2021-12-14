# -- coding: utf-8 --
"""
@Date: 2021/12/10
@Author: Moisthis
@File: urls.py
"""
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from User_Manage.views import *

urlpatterns = [
    path('userinfo/', User_select_myself.as_view(), name='UserInfo'),  # POST 登录接口
    path('userinfo/add',User_add.as_view(),name='AddUser'),
    path('userinfo/delete',User_delete.as_view(),name='DeleteUser'),
    path('userinfo/edit',User_edit.as_view(),name='EditUser'),
    path('userinfo/allinfo',User_select.as_view(),name='SelectALL')


]

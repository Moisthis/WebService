# -- coding: utf-8 --
"""
@Date: 2021/12/10
@Author: Moisthis
@File: urls.py
"""
from django.urls import path
from User_Manage.views import *

urlpatterns = [
    path('userinfo/', User_select_myself.as_view(), name='MyInfo'),
    path('userinfo/add', User_add.as_view(), name='AddUser'),
    path('userinfo/delete', User_delete.as_view(), name='DeleteUser'),
    path('userinfo/edit', User_edit.as_view(), name='EditUser'),
    path('userinfo/allinfo', User_Info, name='ALLUser'),
    path('userinfo/select', User_select.as_view(), name='SelectUser'),
    path('school/', School_Info.as_view(), name='SchoolInfo'),
    path('school/select', School_select.as_view(), name='SchoolSelect'),
    path('school/add', School_add.as_view(), name='SchoolAdd'),
    path('school/delete', School_Delete.as_view(), name='SchoolDelete'),
    path('school/edit', School_edit.as_view(), name='SchoolEdit'),
    path('Department/', Department_Info.as_view(), name='DepartmentInfo'),
    path('Department/select', Department_select.as_view(), name='DepartmentSelect'),
    path('Department/add', Department_add.as_view(), name='DepartmentAdd'),
    path('Department/delete', Department_delete.as_view(), name='DepartmentDelete'),
    path('Department/edit', Department_edit.as_view(), name='DepartmentEdit')
]

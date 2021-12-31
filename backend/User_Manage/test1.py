import json

from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.test import TestCase
from django.forms.models import model_to_dict
# Create your tests here.
from django.core import serializers
import os

if __name__ == '__main__':
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebService.settings')
    import django

    django.setup()
    from User_Manage import models

    # user_obj = models.UserInfo.objects.filter(pk=1).first()
    # user_obj1 = models.UserInfo.objects.filter(pk=2).first()
    # res1 = model_to_dict(user_obj)
    # # res2 = model_to_dict(user_obj1)
    # res2 = {
    #     "data":
    #         {
    #             "id": 101,
    #             "authname": "商品管理",
    #             "userinfo": [res1]
    #         },
    #     "meta":
    #         {
    #             "msg": "获取成功",
    #             "status": 200
    #         }
    # }
    # print(res2['data'])
    # user_dict = models.UserInfo.objects.all().values('id', 'name', 'birthday', 'gender', 'phone')
    # res = list(user_dict)
    # print(res)
    # # user_id = 1
    #     # user_account = models.UserInfo.objects.filter(pk=user_id).first().account
    #     # permission = user_account.permission.permission_grade
    school_obj = models.School.objects.all().values('school_name', 'grade', 'major', 'stu_class', 'post')
    res = list(school_obj)
    print(res)


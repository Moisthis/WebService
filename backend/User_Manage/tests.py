import json

from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.test import TestCase
from django.forms.models import model_to_dict
# Create your tests here.
from django.core import serializers
import os

from django.utils.datetime_safe import datetime

if __name__ == '__main__':
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebService.settings')
    import django

    django.setup()
    from User_Manage import models

    user_obj = models.UserInfo.objects.all()
    user_dict = models.UserInfo.objects.filter(pk=1).values('id', 'name', 'birthday', 'gender', 'phone'
                                                            )

    user_set = []
    for i in user_obj:
        user_set.append(model_to_dict(i))

    res2 = {
        "data":
            {
                "id": 101,
                "authname": "商品管理",
                "userinfo": user_set
            },
        "meta":
            {
                "msg": "获取成功",
                "status": 200
            }
    }
    school_id = models.UserInfo.objects.filter(pk=1).first().school_id
    school_dict = models.School.objects.filter(pk=school_id).values('school_name', 'stu_class', 'grade', 'major')
    # user_dict.update(school_dict)
    res = list(user_dict)+list(school_dict)
    print(res[0]['id'])

    # user_obj[0]['gender'] = user_obj.get_gender_display()
    # user_dict[0]['gender'] = user_obj.get_gender_display()
    # a = {
    #     'data':
    #         {
    #             'id': 101,
    #             'authname': '商品管理',
    #             'userinfo': [
    #                 {
    #                     'id': 1,
    #                     'name': 'sjh',
    #                     'birthday': datetime.date(2021, 12, 12),
    #                     'gender': 1, 'phone': '111',
    #                     'school': 1,
    #                     'account': 1,
    #                 },
    #                 {
    #                     'id': 2,
    #                     'name': 'sll',
    #                     'birthday': datetime.date(2021, 12, 18),
    #                     'gender': 1, 'phone': '222',
    #                     'school': 2,
    #                     'account': 2,
    #                     'department': []
    #                 }
    #             ]
    #         },
    #     'meta': {
    #         'msg': '获取成功',
    #         'status': 200
    #     }
    # }

import json

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

    user_obj = models.UserInfo.objects.filter(pk=1)
    user_obj = serializers.serialize('json', user_obj)
    user = user_obj + user_obj
    my_dict = json.loads(user_obj)
    my_dict1 = json.loads(user_obj)
    my_dict2 = my_dict1 + my_dict
    jsondata = json.dumps(my_dict2,ensure_ascii=False)
    a = JsonResponse(my_dict1,safe=False)
    print(type(a))
    # user_obj = models.UserInfo.objects.filter(pk=1).all()
    # res = serializers.serialize('json',user_obj)
    # print(res)
    # a = JsonResponse(res,
    #                  safe=False)
    # print(a)
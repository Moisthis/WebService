import logging

from django.shortcuts import render

# Create your views here.
import base64
import json
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from User_Manage import models
from django.core import serializers

from rest_framework_jwt.authentication import jwt_decode_handler


def requires_auth(f):
    def inner(request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION').split(" ")[-1]
        user_token = jwt_decode_handler(token)
        user_id = user_token['user_id']
        user_account = models.UserInfo.objects.filter(pk=user_id).first().account
        permission = user_account.permission.permission_grade

        if int(permission) < 3:
            return f(request, *args, **kwargs)
        else:
            return JsonResponse({"msg": "权限不够"},
                                json_dumps_params={"ensure_ascii": False})

    return inner


class User_add(APIView):

    @method_decorator(requires_auth)
    def post(self, request):
        grade = json.loads(request.body.decode().replace("'", "\"")).get('grade')
        school_name = json.loads(request.body.decode().replace("'", "\"")).get('school_name')
        major = json.loads(request.body.decode().replace("'", "\"")).get('major')
        stu_class = json.loads(request.body.decode().replace("'", "\"")).get('stu_class')
        post = json.loads(request.body.decode().replace("'", "\"")).get('post')
        username = json.loads(request.body.decode().replace("'", "\"")).get('username')
        birthday = json.loads(request.body.decode().replace("'", "\"")).get('birthday')
        gender = json.loads(request.body.decode().replace("'", "\"")).get('gender')
        phone = json.loads(request.body.decode().replace("'", "\"")).get('phone')
        account = json.loads(request.body.decode().replace("'", "\"")).get('account')
        password = json.loads(request.body.decode().replace("'", "\"")).get('password')
        school_id = models.School.objects.create(grade=grade,school_name=school_name,major=major,stu_class=stu_class,post=post).id
        models.User.objects.create(username=account,password=password)
        account_id = models.User.objects.filter(username=account).first().id
        models.UserInfo.objects.create(name=username, birthday=birthday,
                                       gender=gender, phone=phone,account_id=account_id,school_id=school_id)
        return JsonResponse({"msg": "success"},
                            json_dumps_params={"ensure_ascii": False})


class User_delete(APIView):
    @method_decorator(requires_auth)
    def post(self, request):
        token = request.META.get('HTTP_AUTHORIZATION').split(" ")[-1]
        user_token = jwt_decode_handler(token)
        user_id = user_token['user_id']
        delete_id = json.loads(request.body.decode().replace("'", "\"")).get('delete_id')
        if user_id == delete_id:
            return JsonResponse({"msg": 'you cannot delete yourself'},
                                json_dumps_params={"ensure_ascii": False})

        res = models.UserInfo.objects.filter(pk=delete_id).first()
        permission = res.account.permission
        you_permission = models.UserInfo.objects.filter(pk=user_id).first().account.permission
        if permission is not None:
            if you_permission < permission:
                return JsonResponse({"msg": 'your permission is low'},
                                    json_dumps_params={"ensure_ascii": False})
        if res is None:
            return JsonResponse({"msg": 'access fail'},
                                json_dumps_params={"ensure_ascii": False})
        else:
            res.delete()
            return JsonResponse({"msg": "success"},
                                json_dumps_params={"ensure_ascii": False})


class User_edit(APIView):
    @method_decorator(requires_auth)
    def post(self, request):
        edit_id = json.loads(request.body.decode().replace("'", "\"")).get('edit_id')
        username = json.loads(request.body.decode().replace("'", "\"")).get('username')
        birthday = json.loads(request.body.decode().replace("'", "\"")).get('birthday')
        gender = json.loads(request.body.decode().replace("'", "\"")).get('gender')
        phone = json.loads(request.body.decode().replace("'", "\"")).get('phone')
        models.UserInfo.objects.filter(id=edit_id).update(
            name=username, birthday=birthday,
            gender=gender, phone=phone
        )
        return JsonResponse({"msg": "success"},
                            json_dumps_params={"ensure_ascii": False})


class User_select(APIView):
    @method_decorator(requires_auth)
    def post(self, request):
        select_way = json.loads(request.body.decode().replace("'", "\"")).get('select_way')
        index = json.loads(request.body.decode().replace("'", "\"")).get('index')
        if select_way == 1:
            res = models.UserInfo.objects.filter(id=index).all().values('id', 'name', 'birthday', 'gender', 'phone')
            return JsonResponse(list(res), safe=False)
        elif select_way == 2:
            res = models.UserInfo.objects.filter(name=index).all().values('id', 'name', 'birthday', 'gender', 'phone')
            return JsonResponse(list(res), safe=False)
        elif select_way == 3:
            res = models.UserInfo.objects.filter(phone=index).all().values('id', 'name', 'birthday', 'gender', 'phone')
            return JsonResponse(list(res), safe=False)
        elif select_way == 2:
            res = models.UserInfo.objects.filter(gender=index).all().values('id', 'name', 'birthday', 'gender', 'phone')
            return JsonResponse(list(res), safe=False)
        # return JsonResponse({"msg": "success"},
        #                     json_dumps_params={"ensure_ascii": False})

    # @requires_auth
    # def get(self, request):
    #     user_obj = models.UserInfo.objects.all()
    #     res = serializers.serialize('json', user_obj)
    #     return JsonResponse(res, safe=False)


class User_Info(APIView):
    @method_decorator(requires_auth)
    def get(self, request):
        user_dict = models.UserInfo.objects.all().values('id', 'name', 'birthday', 'gender', 'phone')
        res = list(user_dict)
        return JsonResponse(res, safe=False)


class User_select_myself(APIView):
    @method_decorator(requires_auth)
    def get(self, request):
        logging.warning(request.META)
        token = request.META.get('HTTP_AUTHORIZATION').split(" ")[-1]
        user_token = jwt_decode_handler(token)
        user_id = user_token['user_id']

        user_dict = models.UserInfo.objects.filter(pk=user_id).values('id', 'name', 'birthday', 'gender', 'phone')
        school_id = models.UserInfo.objects.filter(pk=user_id).first().school_id
        school_dict = models.School.objects.filter(pk=school_id).values('school_name', 'stu_class', 'grade', 'major')
        department = models.UserInfo.objects.filter(pk=user_id).first().department.values('department_name', 'position')
        res = list(user_dict) + list(school_dict) + list(department)

        return JsonResponse(res, safe=False)
        # return HttpResponse("hello")

    # def get(self, request):
    #     return HttpResponse("hello")


class School_add(APIView):
    @requires_auth
    def post(self, request):
        grade = request.POST.get('grade')
        school_name = request.POST.get('school_name')
        major = request.post.get('major')
        stu_class = request.POST.get('stu_class')
        post = request.POST.get('post')
        models.School.objects.create(grade=grade,
                                     school_name=school_name,
                                     major=major,
                                     stu_class=stu_class,
                                     post=post)
        return JsonResponse({"msg": "success"},
                            json_dumps_params={"ensure_ascii": False})


class School_Delete(APIView):
    @requires_auth
    def post(self, request):
        delete_id = request.POST.get('delete_id')
        models.School.objects.filter(pk=delete_id).delete()
        return JsonResponse({"msg": "success"},
                            json_dumps_params={"ensure_ascii": False})


class School_edit(APIView):
    @requires_auth
    def post(self, request):
        edit_id = request.POST.get('id')
        grade = request.POST.get('grade')
        school_name = request.POST.get('school_name')
        major = request.POST.get('major')
        stu_class = request.POST.get('stu_class')
        post = request.POST.get('post')
        models.School.objects.filter(id=edit_id).update(grade=grade,
                                                        school_name=school_name,
                                                        major=major,
                                                        stu_class=stu_class,
                                                        post=post)
        return JsonResponse({"msg": "success"},
                            json_dumps_params={"ensure_ascii": False})


class School_select(APIView):
    @requires_auth
    def post(self, request):
        select_way = request.POST.get('select_way')
        index = request.POST.get('index')
        if select_way == 1:
            user_obj = models.School.objects.filter(id=index)
            res = serializers.serialize('json', user_obj)
            return JsonResponse(res, safe=False)
        elif select_way == 2:
            user_obj = models.School.objects.filter(school_name=index).all()
            res = serializers.serialize('json', user_obj)
            return JsonResponse(res, safe=False)
        elif select_way == 3:
            user_obj = models.School.objects.filter(major=index).all()
            res = serializers.serialize('json', user_obj)
            return JsonResponse(res, safe=False)
        elif select_way == 4:
            user_obj = models.School.objects.filter(grade=index).all()
            res = serializers.serialize('json', user_obj)
            return JsonResponse(res, safe=False)


class School_Info(APIView):
    @requires_auth
    def get(self, request):
        school_obj = models.School.objects.all().values('school_name', 'grade', 'major', 'stu_class', 'post')
        res = list(school_obj)
        return JsonResponse(res, safe=False)


class Department_add(APIView):
    @requires_auth
    def post(self, request):
        department_name = request.POST.get('department_name')
        position = request.POST.get('position')
        incumbency = request.POST.get('incumbency')
        entry_date = request.POST.get('entry_date')
        models.Department_staff.objects.add(department_name=department_name,
                                            position=position,
                                            incumbency=incumbency,
                                            entry_date=entry_date
                                            )
        return JsonResponse({"msg": "success"},
                            json_dumps_params={"ensure_ascii": False})


class Department_delete(APIView):
    @requires_auth
    def post(self, request):
        delete_id = request.POST.get('delete_id')
        models.Department_staff.objects.filter(pk=delete_id).delete()
        return JsonResponse({"msg": "success"},
                            json_dumps_params={"ensure_ascii": False})


class Department_edit(APIView):
    @requires_auth
    def post(self, request):
        edit_id = request.POST.get('edit_id')
        department_name = request.POST.get('department_name')
        position = request.POST.get('position')
        incumbency = request.POST.get('incumbency')
        entry_date = request.POST.get('entry_date')
        models.Department_staff.objects.filter(pk=edit_id).update(
            department_name=department_name,
            position=position,
            incumbency=incumbency,
            entry_date=entry_date
        )


class Department_select(APIView):
    @requires_auth
    def post(self, request):
        select_way = request.POST.get('select_way')
        index = request.POST.get('index')
        if select_way == 1:
            user_obj = models.Department_staff.objects.filter(id=index)
            res = serializers.serialize('json', user_obj)
            return JsonResponse(res, safe=False)
        elif select_way == 2:
            user_obj = models.Department_staff.objects.filter(Department_name=index).all()
            res = serializers.serialize('json', user_obj)
            return JsonResponse(res, safe=False)
        elif select_way == 3:
            user_obj = models.Department_staff.objects.filter(position=index).all()
            res = serializers.serialize('json', user_obj)
            return JsonResponse(res, safe=False)
        elif select_way == 4:
            user_obj = models.Department_staff.objects.filter(incumbency=index).all()
            res = serializers.serialize('json', user_obj)
            return JsonResponse(res, safe=False)


class Department_Info(APIView):
    @requires_auth
    def post(self, request):
        department_dict = models.Department_staff.objects.all().values('department_name', 'position', 'incumbency',
                                                                       'entry_date', 'userinfo__name')

        res = list(department_dict)
        return JsonResponse(res, safe=False)


def require_super(f):
    def inner(request, *args, **kwargs):
        # permisson = request.POST.get('permission')
        # if int(permisson) == 1:
        #     return f(request, *args, **kwargs)
        # return JsonResponse({"msg": '权限不够'},
        #                     json_dumps_params={"ensure_ascii": False})
        token = request.META.get('HTTP_AUTHORIZATION').split(" ")[-1]
        user_token = jwt_decode_handler(token)
        user_id = user_token['user_id']
        user_account = models.UserInfo.objects.filter(pk=user_id).first().account
        permission = user_account.permission.permission_grade
        if int(permission) == 1:
            return f(request, *args, **kwargs)
        return JsonResponse({"msg": "权限不够"},
                            json_dumps_params={"ensure_ascii": False})

    return inner


@require_super
class Permisson_edit(APIView):
    def post(self, request):
        edit_way = request.POST.get('edit_way')
        if edit_way == 1:
            permission_id = request.POST.get('permission_id')
            permission_edit_grade = request.POST.get('grade')
            user_account = models.UserInfo.objects.filter(pk=permission_id).account
            user_account.permission = permission_edit_grade
        elif edit_way == 2:
            permission_id = request.POST.get('permission_id')
            models.UserInfo.objects.filter(pk=permission_id).account.delete()

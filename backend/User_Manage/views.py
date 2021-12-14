from django.shortcuts import render

# Create your views here.
import base64
import json
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from User_Manage import models
from django.core import serializers
from login import models
from rest_framework_jwt.authentication import jwt_decode_handler


def requires_auth(f):
    def inner(request, *args, **kwargs):
        # permission = request.POST.get('permission')
        # if int(permission) < 3:
        #     return f(request, *args, **kwargs)
        # return JsonResponse({"msg": "权限不够"},
        #                     json_dumps_params={"ensure_ascii": False})
        auth = request.stream.META.get('Token')
        user_token = jwt_decode_handler(auth)
        permission = user_token.get('permission')
        if int(permission) < 3:
            return f(request, *args, **kwargs)
        return JsonResponse({"msg": "权限不够"},
                            json_dumps_params={"ensure_ascii": False})

    return inner


class User_add(APIView):

    @requires_auth
    def post(self, request):
        username = request.POST.get('username')
        birthday = request.POST.get('birthday')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        models.UserInfo.objects.create(name=username, birthday=birthday,
                                       gender=gender, phone=phone)
        return JsonResponse({"msg": "success"},
                            json_dumps_params={"ensure_ascii": False})


class User_delete(APIView):
    @requires_auth
    def post(self, request):
        delete_id = request.POST.get('delete_id')
        models.UserInfo.objects.filter(id=delete_id).delete()
        return JsonResponse({"msg": "success"},
                            json_dumps_params={"ensure_ascii": False})


class User_edit(APIView):
    @requires_auth
    def post(self, request):
        edit_id = request.POST.get('edit_id')
        username = request.POST.get('username')
        birthday = request.POST.get('birthday')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        models.UserInfo.objects.filter(id=edit_id).update(
            name=username, birthday=birthday,
            gender=gender, phone=phone
        )
        return JsonResponse({"msg": "success"},
                            json_dumps_params={"ensure_ascii": False})


class User_select(APIView):
    @requires_auth
    def post(self, request):
        select_way = request.POST.get('select_way')
        index = request.POST.get('index')
        if select_way == 1:
            user_obj = models.UserInfo.objects.filter(id=index)
            res = serializers.serialize('json', user_obj)
            return JsonResponse(res, safe=False)
        elif select_way == 2:
            user_obj = models.UserInfo.objects.filter(name=index).all()
            res = serializers.serialize('json', user_obj)
            return JsonResponse(res, safe=False)
        elif select_way == 3:
            user_obj = models.UserInfo.objects.filter(phone=index).all()
            res = serializers.serialize('json', user_obj)
            return JsonResponse(res, safe=False)
        elif select_way == 2:
            user_obj = models.UserInfo.objects.filter(gender=index).all()
            res = serializers.serialize('json', user_obj)
            return JsonResponse(res, safe=False)


class User_select_myself(APIView):
    def post(self, request):
        user_id = request.POST.get('id')
        user_obj = models.UserInfo.objects.filter(pk=user_id)
        user_school_obj = user_obj.school
        user_department_obj = user_obj.depart_set
        res1 = serializers.serialize('json', user_obj)
        res2 = serializers.serialize('json', user_school_obj)
        res3 = serializers.serialize('json',user_department_obj)
        res = res1 + res2 + res3
        return JsonResponse(res, safe=False)


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


def require_super(f):
    def inner(request, *args, **kwargs):
        # permisson = request.POST.get('permission')
        # if int(permisson) == 1:
        #     return f(request, *args, **kwargs)
        # return JsonResponse({"msg": '权限不够'},
        #                     json_dumps_params={"ensure_ascii": False})
        auth = request.stream.META.get('Token')
        user_token = jwt_decode_handler(auth)
        permission = user_token.get('permission')
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

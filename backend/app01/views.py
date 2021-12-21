from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from User_Manage import models
from django.core import serializers
from login import models
from rest_framework_jwt.authentication import jwt_decode_handler


class test(APIView):
    def get(self, request):
        return HttpResponse("hello")

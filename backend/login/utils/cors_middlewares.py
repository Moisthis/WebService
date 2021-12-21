# -- coding: utf-8 --
"""
@Date: 2021/11/17 12:42
@Author: NephrenCake
@File: cors_middlewares.py
"""
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from rest_framework import status
from rest_framework.response import Response


class MyCors(MiddlewareMixin):
    def process_response(self, request, response):
        response["Access-Control-Allow-Origin"] = "*"
        if request.method == "OPTIONS":
            response["Access-Control-Allow-Headers"] = "Origin, Expires, Content-Type, X-E4M-With, Authorization"
            response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST, GET, OPTIONS"
            response.status_code = 200
        return response

    # def process_response(self, request, response):
    #     if request.method == "OPTIONS":
    #         response = HttpResponse(status=200)
    #         response.content = ''
    #         response.content_type = 'application / json;/text/html;charset=UTF-8'
    #         response.status_code = 200
    #
    #     response["Access-Control-Allow-Origin"] = ['127.0.0.1'] or "*"
    #     response["Access-Control-Allow-Headers"] = "Origin, Expires, Content-Type, X-E4M-With, Authorization"
    #     response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST, GET, OPTIONS"
    #     return response

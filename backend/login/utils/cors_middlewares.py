# -- coding: utf-8 --
"""
@Date: 2021/11/17 12:42
@Author: NephrenCake
@File: cors_middlewares.py
"""
from django.utils.deprecation import MiddlewareMixin


class MyCors(MiddlewareMixin):
    def process_response(self, request, response):
        response["Access-Control-Allow-Origin"] = "*"
        if request.method == "OPTIONS":
            response["Access-Control-Allow-Headers"] = "Content-Type"
            response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
        return response

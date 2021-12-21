# -- coding: utf-8 --
"""
@Date: 2021/11/16 20:59
@Author: NephrenCake
@File: get_token.py
"""
from django.contrib.auth import models
from rest_framework_jwt.utils import jwt_decode_handler
from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user):
    # 手动返回令牌
    refresh = RefreshToken.for_user(user)
    user_id = jwt_decode_handler(str(refresh.access_token))["user_id"]
    permission = models.User.objects.filter(pk=user_id).first().permission.permission_grade

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'permission': permission,
        'user_id': user_id
    }

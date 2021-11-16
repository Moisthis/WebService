# -- coding: utf-8 --
"""
@Date: 2021/11/16 20:59
@Author: NephrenCake
@File: get_token.py
"""
from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user):
    # 手动返回令牌
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# -- coding: utf-8 --
"""
@Date: 2021/11/16 20:59
@Author: NephrenCake
@File: get_token.py
"""
from rest_framework_simplejwt.tokens import RefreshToken
from login import models
from User_Manage import models


def get_tokens_for_user(user):
    # 手动返回令牌
    refresh = RefreshToken.for_user(user)
    user_id = refresh.get('user')
    user_account = models.User.objects.filter(pk=user_id).account
    permission = user_account.permission
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'permission': int(permission),
    }

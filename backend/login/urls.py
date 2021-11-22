# -- coding: utf-8 --
"""
@Date: 2021/11/16 21:09
@Author: NephrenCake
@File: urls.py
"""
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from login.views import CaptchaAPIView, DmallTokenObtainPairView, test, test_no_login

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # POST 登录接口
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # POST 刷新token接口
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),  # POST 验证token接口

    path('captcha/', CaptchaAPIView.as_view(), name='captcha_api'),  # GET 返回验证码接口
    path('captcha/token/', DmallTokenObtainPairView.as_view(), name='mytoken'),

    path('test/', test.as_view(), name='test'),
    path('no_login/', test_no_login.as_view(), name='test'),
]

from django.urls import path
from app01.views import *

urlpatterns = [
    path('test/', test.as_view(), name='MyInfo'),

]

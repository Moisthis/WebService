from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User, AbstractUser


class permission(models.Model):
    # permission grade
    permission_choices = ((1, 'superadmin'), (2, 'admin'), (3, 'user'))
    permission_grade = models.SmallIntegerField(choices=permission_choices)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    '''
    普通用户只能注册自己的个人信息和学院信息,但关于部门的信息需要管理员注册
    管理员可以浏览各个信息，并且帮助普通用户注册并修改部门信息
    超级管理员不仅可以具有管理员的权限，还可以任命或罢免普通用户的信息
    '''

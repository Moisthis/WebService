from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User, AbstractUser


class UserInfo(models.Model):
    name = models.CharField(max_length=20, verbose_name="姓名", blank=False)
    birthday = models.DateField('生日', blank=False)
    # 性别
    gender_choice = ((1, '男'), (2, '女'))
    gender = models.SmallIntegerField(choices=gender_choice, blank=False)
    phone = models.CharField(max_length=20, verbose_name="电话号码", blank=False)
    department = models.ManyToManyField(to='Department_staff')
    school = models.OneToOneField(to='School', on_delete=models
                                  .CASCADE)
    account = models.OneToOneField(to=User, on_delete=models.CASCADE)


class Department_staff(models.Model):
    department_name = models.CharField(max_length=20, verbose_name="部门名", blank=True)
    position = models.CharField(max_length=20, verbose_name="职位", blank=True)
    incumbency = models.CharField(max_length=20, verbose_name="在职情况", blank=True)
    entry_date = models.DateField('入职时间', blank=True)


class School(models.Model):
    grade = models.IntegerField(verbose_name='学生的年级', blank=False)
    school_name = models.CharField(max_length=20, verbose_name="学院名", blank=False)
    major = models.CharField(max_length=20, verbose_name="专业名", blank=False)
    stu_class = models.IntegerField(verbose_name="班级", blank=False)
    # 职务
    post_choice = ((1, '班长'), (2, '团委'), (3, '学习委员'),
                   (4, '宣传委员'), (5, '体育委员'), (6, '劳动委员'), (7, '无职位'))
    post = models.SmallIntegerField(choices=post_choice, blank=False)

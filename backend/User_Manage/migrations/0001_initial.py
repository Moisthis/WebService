# Generated by Django 3.2.9 on 2022-01-04 15:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department_staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(blank=True, max_length=20, verbose_name='部门名')),
                ('position', models.CharField(blank=True, max_length=20, verbose_name='职位')),
                ('incumbency', models.CharField(blank=True, max_length=20, verbose_name='在职情况')),
                ('entry_date', models.DateField(blank=True, verbose_name='入职时间')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField(verbose_name='学生的年级')),
                ('school_name', models.CharField(max_length=20, verbose_name='学院名')),
                ('major', models.CharField(max_length=20, verbose_name='专业名')),
                ('stu_class', models.IntegerField(verbose_name='班级')),
                ('post', models.SmallIntegerField(choices=[(1, '班长'), (2, '团委'), (3, '学习委员'), (4, '宣传委员'), (5, '体育委员'), (6, '劳动委员'), (7, '无职位')])),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('birthday', models.DateField(verbose_name='生日')),
                ('gender', models.SmallIntegerField(choices=[(1, '男'), (2, '女')])),
                ('phone', models.CharField(max_length=20, verbose_name='电话号码')),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('department', models.ManyToManyField(to='User_Manage.Department_staff')),
                ('school', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='User_Manage.school')),
            ],
        ),
    ]
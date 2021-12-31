# Generated by Django 3.2.9 on 2021-12-29 09:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('User_Manage', '0004_userinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User_Manage.school'),
        ),
    ]
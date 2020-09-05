from django.db import models

# Create your models here.
# 普通用户类
class Users(models.Model):
    user_id = models.CharField(max_length=50, default='None')
    user_name = models.CharField(max_length=50, default='None')
    user_sex = models.CharField(max_length=10, default='None')
    user_birth = models.CharField(max_length=50, default='None')
    user_password = models.CharField(max_length=50, default='None')
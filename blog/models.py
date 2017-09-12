from django.db import models
from captcha.fields import CaptchaField

# Create your models here.


# 用户注册/登录信息
class User(models.Model):
    email = models.EmailField(blank=False)
    password = models.CharField(blank=False, max_length=100)








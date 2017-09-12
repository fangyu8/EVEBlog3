from django import forms
from captcha.fields import CaptchaField


# 验证码
class RegisterForm(forms.Form):
    captcha = CaptchaField(error_messages={"invalid": "验证码错误"})

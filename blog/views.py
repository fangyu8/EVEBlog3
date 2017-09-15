from django.shortcuts import render, HttpResponse

from blog.forms import RegisterForm
from django import forms
from .models import User
from captcha.fields import CaptchaField, CaptchaStore
from captcha.helpers import captcha_image_url


# Create your views here.

# 主页面
def index(request):
    return render(request, 'blog/index.html')


# 注册表单
class UserFormRegister(forms.Form):
    email = forms.EmailField(max_length=100)
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})


# 登录表单
class UserFormLogin(forms.Form):
    email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})


# 登录页面
def login(request):
    user_formlogin = UserFormLogin()
    return render(request, 'blog/login.html', {'user_formlogin': user_formlogin})


# 登录操作页面
def login_action(request):
    # # 刷新验证码
    # if request.GET.get('newsn') == '1':
    #     csn = CaptchaStore.generate_key()
    #     cimageurl = captcha_image_url(csn)
    #     return HttpResponse(cimageurl)

    if request.method == 'POST':
        user_formlogin = UserFormLogin(request.POST)
        if user_formlogin.is_valid():
            # 获取表单信息
            email = user_formlogin.cleaned_data['email']
            password = user_formlogin.cleaned_data['password']
            errors = []
            # 获得的表单数据与数据库进行比较
            user_result = User.objects.filter(email__exact=email, password__exact=password)

            if user_result:
                # 如果比较成功，则跳转主页index.html
                response = render(request, 'blog/login_success.html', locals())
                response.set_cookie('email', email, 3600)
                return response
            else:
                # 如果比较失败，则仍在login.html
                return render(request, 'blog/login.html', {'errors': '该用户名不存在'}, locals())

    else:
        user_formlogin = UserFormLogin()
    return render(request, 'blog/login.html', {'user_formlogin': user_formlogin}, locals())


# 注册页面
def register(request):
    user_formregister = UserFormRegister()
    return render(request, 'blog/register.html', {'user_formregister': user_formregister}, locals())


# 注册操作页面
def register_action(request):
    if request.method == 'POST':
        user_formregister = UserFormRegister(request.POST)
        if user_formregister.is_valid():
            # 获取表单数据
            email = user_formregister.cleaned_data['email']
            password = user_formregister.cleaned_data['password1']
            password1 = user_formregister.cleaned_data['password1']
            password2 = user_formregister.cleaned_data['password2']

            if User.objects.filter(email__exact=email):
                return render(request, 'blog/register.html', {'errors': '该用户名已存在'})

            if password2 != password1:
                return render(request, 'blog/register.html', {'errors': '两次输入密码不一致'})

            # 添加到数据库中
            user = User.objects.create(email=email, password=password)
            user.save()
            # 返回注册成功页面
            return render(request, 'blog/login_success.html', {'email': email})

    else:
        user_formregister = UserFormRegister()
    return render(request, 'blog/register.html', {'user_formregister': user_formregister})


# 忘记密码页面
def forget(request):
    return render(request, 'blog/forget.html')

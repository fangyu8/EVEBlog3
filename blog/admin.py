from django.contrib import admin
from blog.models import User

# Register your models here.

# 在admin中注册绑定
@admin.register(User)
# Blog模型的管理器
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'password')

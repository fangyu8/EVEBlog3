from django.contrib import admin
from blog.models import Article

# Register your models here.

# 在admin中注册绑定
@admin.register(Article)
# Blog模型的管理器
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')

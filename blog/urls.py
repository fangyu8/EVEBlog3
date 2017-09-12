from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^reg/$', views.register, name='register'),
    url(r'^forget/$', views.forget, name='forget'),

]

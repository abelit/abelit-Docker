"""dataforum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from home import views as home_views

urlpatterns = [
    url(r'^$', home_views.index, name='index'),
    url(r'^accounts/login/', home_views.login, name='login'),
    url(r'^accounts/logout/', home_views.logout, name='logout'),
    url(r'^accounts/register/', home_views.register, name='register'),
    url(r'^accounts/forgot_password/', home_views.forgot_password, name='forgot_password'),
    url(r'^accounts/change_password/', home_views.change_password, name='change_password'),
    url(r'^accounts/verify_code/', home_views.verify_code, name='verify_code'),
    # url(r'^accounts/reset_password/', home_views.reset_password, name='reset_password'),

    # test ajax
    url(r'^add/$', home_views.add, name='home_add'),
    url(r'^add/add_ajax/$', home_views.add_ajax, name='home_add_ajax'),
    url(r'^time/time_ajax/$', home_views.time_ajax, name='home_time_ajax'),
    url(r'^ajax_list/$', home_views.ajax_list, name='home_ajax_list'),
    url(r'^ajax_dict/$', home_views.ajax_dict, name='home_ajax_dict'),
    url(r'^list_user/$', home_views.list_user, name='list_user'),
]

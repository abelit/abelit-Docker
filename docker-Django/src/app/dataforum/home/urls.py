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
from home import views as home_views

urlpatterns = [
    url(r'^$', home_views.index, name='index'),
    
    # test ajax
    url(r'^add/$', home_views.add, name='home_add'),
    url(r'^add/add_ajax/$', home_views.add_ajax, name='home_add_ajax'),
    url(r'^time/time_ajax/$', home_views.time_ajax, name='home_time_ajax'),
    url(r'^ajax_list/$', home_views.ajax_list, name='home_ajax_list'),
    url(r'^ajax_dict/$', home_views.ajax_dict, name='home_ajax_dict'),
    url(r'^list_user/$', home_views.list_user, name='list_user'),
]

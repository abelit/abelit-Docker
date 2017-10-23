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
from report import views as report_views

urlpatterns = [
    url(r'^$', report_views.index, name='index'),

    url(r'^host/add/$',report_views.host_add, name='host_add'),
    url(r'^host/list/$',report_views.get_host_list, name='get_host_list'),
    
    # url(r'^host/detail/(\d+)/$',report_views.get_host_detail, name='get_host_detail'),
    # url(r'^host/oracle/add/(\d+)/$',report_views.oracle_add, name='oracle_add'),
    # url(r'^host/oracle/del/(\d+)/$',report_views.oracle_del, name='oracle_del'),
]

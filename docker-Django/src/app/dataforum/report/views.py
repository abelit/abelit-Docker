from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.context_processors import request
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import Http404
import datetime
from report.models import Host, Oracle, HostMetric,OracleMetric
from report.forms import HostForm, OracleForm
import json


# Create your views here.

def index(request):
    #return HttpResponse(u"欢迎光临 abelit的网站!")
    today = datetime.datetime.now().date()
    return render(request, 'report/index.html',{'today': today})

def host_add(request):
    if request.method == 'GET':
        form = HostForm()
    else:
        form = HostForm(request.POST)

        if form.is_valid():
            cleaned_data = form.cleaned_data
            # return HttpResponse(json.dumps(cleaned_data, sort_keys=True, indent=4, separators=(',', ': '))) #test
            Host.objects.create(**cleaned_data)
            return HttpResponseRedirect(reverse("report:host_list"))
    return render(request,'report/host_add.html',{'form':form})

def host_delete(request, id=None):
    host = get_object_or_404(Host, pk=int(id))

#     return HttpResponse(HostMetric.objects.get(host=host).status) #test
    host.delete()
    return HttpResponseRedirect(reverse("report:host_list"))

def host_update(request, id=None):
    host = get_object_or_404(Host, pk=int(id))
    if request.method == 'POST':
        form = HostForm(request.POST, instance=host)
        if form.is_valid():
            host = form.save()
            return HttpResponseRedirect(reverse("report:host_list"))
    return render(request,'report/host_add.html',{'form':HostForm(instance=host)})

def host_list(request):
    """
    List all Hosts
    """
    host_list = Host.objects.all()
    paginator = Paginator(host_list,10)

    # host_metric_list = HostMetric.objects.all()
    # host_metric_dict = {}
    # for host_metric in host_metric_list.values('host_id'):
    #     host_metric_dict.setdefault(host_metric['host_id'],HostMetric.objects.get(host_id=host_metric['host_id']).status)
    # # return HttpResponse(host_metric_dict.values())

    # host_metric_list = HostMetric.objects.all()
    # host_metric_dict = {}
    # for (key,value) in host_metric_list.values_list('host_id','status'):
    #     host_metric_dict.setdefault(key,value)

#     host = []
#     for i in host_list:
#         host.append(i)

#     #主键关联外建
#     host = HostMetric.objects.get(host_id=5)
#     return HttpResponse(host.host.name)

#     host = HostMetric.objects.filter(host_id=15).latest('id')
#     return HttpResponse(host.status)

#     #外建关联逐渐
#     host = Host.objects.get(id=5)
#     return HttpResponse(host.hostmetric_set.latest ("id").status)

#     host = Host.objects.get(id=15)
#     hm = host.hostmetric_set.latest ('id')
#     test = {host.id:{'name':host.name,'ipaddress':host.ipaddress,'username':host.username,'status':hm.status}}
#
#     return HttpResponse(json.dumps(test))

    hostmetric_list = []
    for hl in host_list.values('id'):
        host = Host.objects.get(id=hl['id'])
        if host.hostmetric_set.all():
            hostmetric = host.hostmetric_set.latest('id')
            hostmetric_list.append({'id':host.id,'name':host.name,'ipaddress':host.ipaddress,'ssh_port':host.ssh_port,'username':host.username,'hostmetric_status':hostmetric.status})
        else:
            hostmetric_list.append({'id':host.id,'name':host.name,'ipaddress':host.ipaddress,'ssh_port':host.ssh_port,'username':host.username,'hostmetric_status':'unknown'})

#     return HttpResponse(json.dumps(hostmetric_list))

    try:
        page = int(request.GET.get('page','1'))
    except ValueError:
        page = 1

    try:
        host_list = paginator.page(page)
    except :
        all_host = paginator.page(paginator.num_pages)

    return render(request, 'report/host_list.html', {'host_list': host_list, 'hostmetric_list':hostmetric_list, 'page': page, 'paginator':paginator})

def host_detail(request):
    return render(request,'report/host_detail.html')

def host_metric(request, id=None):
#     host = get_object_or_404(Host, pk=int(id))
#     return HttpResponse(HostMetric.objects.get(host=host).status)
    host = Host.objects.get(id=id)
    hostmetric_list = []
    if host.hostmetric_set.all():
        hostmetric = host.hostmetric_set.latest('id')
        hostmetric_list.append({'id':host.id,'name':host.name,'ipaddress':host.ipaddress,'ssh_port':host.ssh_port,'username':host.username,'hostmetric_status':hostmetric.status})
    else:
        hostmetric_list.append({'id':host.id,'name':host.name,'ipaddress':host.ipaddress,'ssh_port':host.ssh_port,'username':host.username,'hostmetric_status':'unknown'})

    return HttpResponse(json.dumps(hostmetric_list))

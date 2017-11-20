from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.context_processors import request
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import Http404
import datetime
from report.models import Host, Oracle
from report.forms import HostForm, OracleForm

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
            Host.objects.create(**cleaned_data)
            return HttpResponseRedirect(reverse("report:host_list"))
    return render(request,'report/host_add.html',{'form':form})

def host_delete(request, id=None):
    host = get_object_or_404(Host, pk=int(id))
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

def host_metric(request, id=None):
    pass


def host_list(request):
    """
    List all Hosts
    """
    host_list = Host.objects.all()
    paginator = Paginator(host_list,10)

    try:
        page = int(request.GET.get('page','1'))
    except ValueError:
        page = 1

    try:
        host_list = paginator.page(page)
    except :
        all_host = paginator.page(paginator.num_pages)

    return render(request, 'report/host_list.html', {'host_list': host_list, 'page': page, 'paginator':paginator})

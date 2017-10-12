from django.shortcuts import render
from django.http import HttpResponse
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
    return render(request,'report/host_add.html',{'form':form})


def get_host_list(request):
    """
    List all Hosts
    """
    host_list = Host.objects.all()
    # host_list = Host.objects.all()
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

def manage_host(request, id=None):   # 负责添加和修改和删除主机，删除，修改主机需要提供id号
    if id:
        host_list = get_object_or_404(HostList, pk=id)
        action = 'edit'
        # page_name = '编辑主机'

    else:
        host_list = HostList()
        action = 'add'
        # page_name = '新增主机'
        ret=[]

    if request.method == 'GET':
        delete = request.GET.get('delete')
        id = request.GET.get('id')
        if delete:
            Message.objects.create(type='host', action='manage', action_ip=ret, content='主机下架')
            host_list = get_object_or_404(HostList, pk=id)
            host_list.delete()
            return HttpResponseRedirect(reverse('host_list'))
    if request.method == 'POST':    # 修改主机或者添加新主机
        form = HostsListForm(request.POST,instance=host_list)
        print request.POST
        operate = request.POST.get('operate')  # 这里表示点击更新了按钮
        if form.is_valid():
            if action == 'add':   #  点击添加按钮
                form.save()
                ret.append(form.cleaned_data['ip'])
                Message.objects.create(type='host', action='manage', action_ip=ret, content='主机添加成功')
                return HttpResponseRedirect(reverse('host_list'))
            if operate:
                if operate == 'update':
                    form.save()
                    Message.objects.create(type='host', action='manage', action_ip=ret, content='主机信息更新')
                    return HttpResponseRedirect(reverse('host_list'))
                else:
                    pass
    else:
        form = HostsListForm(instance=host_list)

    return render(request, 'report/host_manage.html',
           {"form": form,
            # "page_name": page_name,
            "action": action,  # 这里action 要注意 如果是edit 页面显示edit按钮 如果是add页面显示add按钮
           })


# def get_host_detail(request,server_id):
#     server = Server.objects.get(id=server_id)
#     oracleserver = server.oracleserver_set.all()
#     return render(request, 'report/host_detail.html', {'server':server,'oracleserver':oracleserver})

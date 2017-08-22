from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
# 首页
def index(request):
    return render(request, 'home/index.html')

# test ajax
@login_required
def add(request):
    return render(request, 'home/testajax.html')

def add_ajax(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    # return HttpResponse(a)
    return HttpResponse(str(a+b))

def time_ajax(request):
    # c = request.POST['c']
    d = request.POST['d']
    c = request.POST.get('c')
    e = request.POST.get('e')
    # d = request.POST.get('d')
    c = int(c)
    d = int(d)
    e = int(e)
    return JsonResponse({"result":str(c*e)})

def ajax_list(request):
    a = range(100)
    return JsonResponse(json.dumps(a))

def ajax_dict(request):
    name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    return JsonResponse(name_dict)

@login_required
def list_user(request):
    u = User.objects.all()

    return render(request, 'home/user.html', {"userlist":u})

def list_user_handler(request):
    pass

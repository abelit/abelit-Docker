from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import json


# Create your views here.
# 首页
def index(request):
    return render(request, 'home/index.html')

# test ajax
@login_required
def ajax_test(request):
    return render(request, 'home/ajax_test.html')

def ajax_add(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a+b))

def ajax_time(request):
    c = request.POST['c']
    d = request.POST['d']
    c = int(c)
    d = int(d)
    return JsonResponse({"result":str(c*d)})

def ajax_list(request):
    a = range(100)
    return JsonResponse(a)

def ajax_dict(request):
    name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    return JsonResponse(name_dict)

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'home/user_list.html', {"users":users})

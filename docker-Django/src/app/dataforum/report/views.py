from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.template.context_processors import request
# Create your views here.

def index(request):
    #return HttpResponse(u"欢迎光临 abelit的网站!")
    today = datetime.datetime.now().date()
    return render(request, 'report/index.html',{'today': today})

def oracle(request):
    return render(request, 'report/oracle.html')
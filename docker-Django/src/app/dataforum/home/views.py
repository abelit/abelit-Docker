from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def index(request):
    #return HttpResponse(u"欢迎光临 abelit的网站!")
    today = datetime.datetime.now().date()
    return render(request, 'home.html',{'today': today})

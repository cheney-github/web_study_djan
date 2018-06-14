from django.shortcuts import render
from django.http import HttpResponse
from .models import Page,Wenzhang

# Create your views here.


def homepage(request):
    data = Page.objects.all()
    data2 = Wenzhang.objects.all()
    return render(request,'index.html',{'data':data,'data2':data2})



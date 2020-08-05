from django.shortcuts import render

# Create your views here.
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage,InvalidPage
from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return render(request, 'index.html', locals())

def showpost(request):
        return render(request,'info.html',locals())


def showpost1(request):
    return render(request, 'info1.html', locals())

def showpost2(request):
    return render(request, 'info2.html', locals())

def showpost3(request):
    return render(request, 'info3.html', locals())

def showpost4(request):
    return render(request, 'info4.html', locals())

def showpost5(request):
    return render(request, 'info5.html', locals())

def showpost6(request):
    return render(request, 'info6.html', locals())

def showpost7(request):
    return render(request, 'info7.html', locals())

def showpost8(request):
    return render(request, 'info8.html', locals())
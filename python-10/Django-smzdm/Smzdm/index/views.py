from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello World!")

def myyear(request, year):
    return HttpResponse("Hello,xxx")

def abc(request, **kwargs):
    print (kwargs)
    return HttpResponse("ABC")

def re_year(request, year):
    return HttpResponse("re_year")

def mmm(request, **kwargs):
    return HttpResponse("mmm")
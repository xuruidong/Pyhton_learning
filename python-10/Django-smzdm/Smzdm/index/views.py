#! 
from django.shortcuts import render
from django.http import HttpResponse
from .models import SmzdmResult
# Create your views here.

def index(request):
    return HttpResponse("Hello World!")

def myyear(request, year):
    # return HttpResponse("Hello, %s" % year)
    return render(request, 'vartest.html', locals())

def abc(request, **kwargs):
    print (kwargs)
    return HttpResponse("ABC")

def re_year(request, year):
    return HttpResponse("re_year")

def mmm(request, **kwargs):
    return HttpResponse("mmm")

def comment(request, **kwargs):
    # res = SmzdmResult.objects.all()
    # return render(request, 'comment_result.html', locals())
    shorts = SmzdmResult.objects.all()
    # comment counts
    counter = SmzdmResult.objects.all().count()  
    # positive 
    queryset = SmzdmResult.objects.values('sentiment')
    condtions = {'sentiment__gte': 0.5}
    plus = queryset.filter(**condtions).count()

    # negative
    queryset = SmzdmResult.objects.values('sentiment')
    condtions = {'sentiment__lt': 0.5}
    minus = queryset.filter(**condtions).count()

    # return render(request, 'douban.html', locals())
    return render(request, 'result.html', locals())    

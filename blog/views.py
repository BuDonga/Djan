from django.http import HttpResponse
from django.shortcuts import render
import datetime


def hello(request):
    return HttpResponse('<h1>Hello World!</h1>')


def error(request):
    return HttpResponse('<h1>Not Found!</h1>')


def current_time(request):
    now = datetime.datetime.now()
    return HttpResponse('<html><body>now the time is %s!</body></html>' % now)

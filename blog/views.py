from django.http import HttpResponse, Http404
from django.shortcuts import render, render_to_response
import datetime

from django.template import Template, Context
from django.template.loader import get_template


def hello(request):
    return HttpResponse('<h1>Hello World!</h1>')


def error(request):
    return HttpResponse('<h1>Not Found!</h1>')


def current_time(request, ahead):
    try:
        ahead = int(ahead)
    except ValueError:
        raise Http404()
    now = datetime.datetime.now()
    #return HttpResponse('<html><body>now the time is %s!</body></html>' % now)
    a = {'now': now, 'ahead': ahead}
    # html = get_template('current_datetime.html')
    # c = Context({'a': a})
    # a = html.render(c)
    # return HttpResponse(a)
    return render_to_response('current_datetime.html', {'a': a})


def includes(request):
    a = {'title': 'this is a title !!!!!!!', 'current_section': 'current section is including'}
    return render_to_response('mypage.html', {'a': a})









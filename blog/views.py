from django.http import HttpResponse, Http404
from django.shortcuts import render
import datetime

from django.template import Template, Context


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
    html = Template('<html><body>now the time is {{a.now}}! and it\'s ahead {{a.ahead}} hours</body></html>')
    c = Context({'a': a})
    a = html.render(c)
    return HttpResponse(a)








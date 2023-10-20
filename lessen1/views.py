import datetime
from os import listdir

from django.shortcuts import render, reverse

def time(request):
    template_name = 'lessen1/time.html'
    time_msg = datetime.datetime.now().time().strftime("%H:%M:%S")

    ctx = {'time': time_msg}

    return render(request, template_name, context=ctx)

def home(request):
    dict_urls = {'Время': reverse('time'),
                 'Список дирикторий': reverse('workdir')}

    ctx = {'dict_urls': dict_urls}

    templates_name = 'lessen1/home.html'
    return render(request, templates_name, context=ctx)

def workdir(request):
    rez = listdir(path='.')
    templates_name = 'lessen1/workdir.html'

    ctx = {'rez': rez}
    return render(request, templates_name, context=ctx)
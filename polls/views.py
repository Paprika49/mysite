from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def index(request):
    return render(request, 'polls/index.html', {})

def target(request):
    return render(request, 'polls/target.html', {})

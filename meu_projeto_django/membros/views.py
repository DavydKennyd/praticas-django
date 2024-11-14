from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def membros(request):
    template = loader.get_template('primeiro.html')
    return HttpResponse(template.render())

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def homepage(request):
    template = 'templates/homepage.html'
    context = {'username':request.environ['USERNAME']}
    return render(request, template, context)
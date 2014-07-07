from django.shortcuts import render
from django.template import RequestContext


def home_page(request):
    return render(request, 'lists/home.html')

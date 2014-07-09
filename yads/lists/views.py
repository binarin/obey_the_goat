from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse


def home_page(request):
    data = {}
    if request.method == 'POST':
        data['new_item_text'] = request.POST['item_text']
    return render(request, 'lists/home.html', data)

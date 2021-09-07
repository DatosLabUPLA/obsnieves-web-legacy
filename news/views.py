from django.shortcuts import render
from .models import New, Origin
from django import template

# Create your views here.
def news(request):
    n = New.objects.all()

    context = {
        'news': n,
    }
    return render(request, 'news/news.html', context)

def detail_new(request, pk):
    n = New.objects.get(id = pk)
    context = {
        'new': n,
    }
    return render(request, 'news/detail_new.html', context)





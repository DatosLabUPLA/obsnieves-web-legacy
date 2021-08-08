from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def team(request):
    return render(request, 'core/team.html')

def database(request):
    return render(request, 'core/database.html')

def display(request):
    return render(request, 'core/display.html')

def news(request):
    return render(request, 'core/news.html')

def events(request):
    return render(request, 'core/events.html')

def error_404(request, exception):
    data = {}
    return render(request,'core/error_404.html', data)

def error_500(request):
    data = {}
    return render(request,'core/error_500.html', data)


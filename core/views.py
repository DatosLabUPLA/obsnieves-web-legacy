from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def team(request):
    return render(request, 'core/team.html')

def team_director(request):
    return render(request, 'core/team_director.html')

def team_investigator(request):
    return render(request, 'core/team_investigator.html')

def team_professional(request):
    return render(request, 'core/team_professional.html')

def team_students(request):
    return render(request, 'core/team_students.html')

def team_lab(request):
    return render(request, 'core/team_lab.html')

def team_associate(request):
    return render(request, 'core/team_associate.html')

def team_collab(request):
    return render(request, 'core/team_collab.html')


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


from django.shortcuts import render
from .models import Team, Position

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def team(request):
    team = Team.objects.all()
    positions = Position.objects.order_by('index')

    team_members = []
    for position in positions:
        team_members.append({
            'position': position.name,
            'members': team.filter(id_position=position.id).order_by('index'),
        })

    context = {
        'teams':team_members,
    }
    return render(request, 'core/team.html', context)

def team_lab(request):
    return render(request, 'core/team_lab.html')


def database(request):
    return render(request, 'core/database.html')

def escalation(request):
    return render(request, 'core/escalation.html')


def display_description(request):
    return render(request, 'core/display_description.html')

def display_landsat(request):
    return render(request, 'core/display_landsat.html')

def display_modis(request):
    return render(request, 'core/display_modis.html')

def display_sentinel(request):
    return render(request, 'core/display_sentinel.html')


def events(request):
    return render(request, 'core/events.html')

def error_404(request, exception):
    data = {}
    return render(request,'core/error_404.html', data)

def error_500(request):
    data = {}
    return render(request,'core/error_500.html', data)

def map_1(request):
    return render(request, 'core/map_1.html')

def map_2(request):
    return render(request, 'core/map_2.html')

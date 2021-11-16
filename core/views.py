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

def landsat_1989(request):
    return render(request, 'maps/landsat/1989_Landsat.html')

def landsat_1990(request):
    return render(request, 'maps/landsat/1990_Landsat.html')

def landsat_1991(request):
    return render(request, 'maps/landsat/1991_Landsat.html')

def landsat_1992(request):
    return render(request, 'maps/landsat/1992_Landsat.html')

def landsat_1993(request):
    return render(request, 'maps/landsat/1993_Landsat.html')

def landsat_1994(request):
    return render(request, 'maps/landsat/1994_Landsat.html')

def landsat_1995(request):
    return render(request, 'maps/landsat/1995_Landsat.html')

def landsat_1996(request):
    return render(request, 'maps/landsat/1996_Landsat.html')

def landsat_1997(request):
    return render(request, 'maps/landsat/1997_Landsat.html')

def landsat_1998(request):
    return render(request, 'maps/landsat/1998_Landsat.html')

def landsat_1999(request):
    return render(request, 'maps/landsat/1999_Landsat.html')

def landsat_2000(request):
    return render(request, 'maps/landsat/2000_Landsat.html')

def landsat_2001(request):
    return render(request, 'maps/landsat/2001_Landsat.html')

def landsat_2002(request):
    return render(request, 'maps/landsat/2002_Landsat.html')

def landsat_2003(request):
    return render(request, 'maps/landsat/2003_Landsat.html')

def landsat_2004(request):
    return render(request, 'maps/landsat/2004_Landsat.html')

def landsat_2005(request):
    return render(request, 'maps/landsat/2005_Landsat.html')

def landsat_2006(request):
    return render(request, 'maps/landsat/2006_Landsat.html')

def landsat_2007(request):
    return render(request, 'maps/landsat/2007_Landsat.html')

def landsat_2008(request):
    return render(request, 'maps/landsat/2008_Landsat.html')

def landsat_2009(request):
    return render(request, 'maps/landsat/2009_Landsat.html')

def landsat_2010(request):
    return render(request, 'maps/landsat/2010_Landsat.html')

def landsat_2011(request):
    return render(request, 'maps/landsat/2011_Landsat.html')

def landsat_2012(request):
    return render(request, 'maps/landsat/2012_Landsat.html')

def landsat_2013(request):
    return render(request, 'maps/landsat/2013_Landsat.html')

def landsat_2014(request):
    return render(request, 'maps/landsat/2014_Landsat.html')

def landsat_2015(request):
    return render(request, 'maps/landsat/2015_Landsat.html')

def landsat_2016(request):
    return render(request, 'maps/landsat/2016_Landsat.html')

def landsat_2017(request):
    return render(request, 'maps/landsat/2017_Landsat.html')

def landsat_2018(request):
    return render(request, 'maps/landsat/2018_Landsat.html')

def landsat_2019(request):
    return render(request, 'maps/landsat/2019_Landsat.html')

def landsat_2020(request):
    return render(request, 'maps/landsat/2020_Landsat.html')
"""obsnievesweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from core import views as core_views
from news import views as news_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', core_views.home, name='home'),

    path('equipo/', core_views.team, name='team'),
    path('equipo/entidades/', core_views.team_lab, name='team_lab'),

    path('basededatos/', core_views.database, name='database'),
    path('escalamiento/', core_views.escalation, name='escalation'),

    path('visualizadores/', core_views.display_description, name='display_description'),
    path('visualizadores/landsat/', core_views.display_landsat, name='display_landsat'),
    path('visualizadores/modis/', core_views.display_modis, name='display_modis'),
    path('visualizadores/sentinel/', core_views.display_sentinel, name='display_sentinel'),

    path('noticias/', news_views.news, name='news'),
    path('noticias/<int:pk>', news_views.detail_new, name='detail_new'),


    path('eventos/', core_views.events, name='events'),

    # Modificar para las pruebas del código generado
    path('prueba/', core_views.events, name='events'),

    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('map_1', core_views.map_1, name='map_1'),
    path('map_2', core_views.map_2, name='map_2'),

    path('landsat_1989', core_views.landsat_1989, name='landsat_1989'),
    path('landsat_1990', core_views.landsat_1990, name='landsat_1990'),
    path('landsat_1991', core_views.landsat_1991, name='landsat_1991'),
    path('landsat_1992', core_views.landsat_1992, name='landsat_1992'),
    path('landsat_1993', core_views.landsat_1993, name='landsat_1993'),
    path('landsat_1994', core_views.landsat_1994, name='landsat_1994'),
    path('landsat_1995', core_views.landsat_1995, name='landsat_1995'),
    path('landsat_1996', core_views.landsat_1996, name='landsat_1996'),
    path('landsat_1997', core_views.landsat_1997, name='landsat_1997'),
    path('landsat_1998', core_views.landsat_1998, name='landsat_1998'),
    path('landsat_1999', core_views.landsat_1999, name='landsat_1999'),
    path('landsat_2000', core_views.landsat_2000, name='landsat_2000'),
    path('landsat_2001', core_views.landsat_2001, name='landsat_2001'),
    path('landsat_2002', core_views.landsat_2002, name='landsat_2002'),
    path('landsat_2003', core_views.landsat_2003, name='landsat_2003'),
    path('landsat_2004', core_views.landsat_2004, name='landsat_2004'),
    path('landsat_2005', core_views.landsat_2005, name='landsat_2005'),
    path('landsat_2006', core_views.landsat_2006, name='landsat_2006'),
    path('landsat_2007', core_views.landsat_2007, name='landsat_2007'),
    path('landsat_2008', core_views.landsat_2008, name='landsat_2008'),
    path('landsat_2009', core_views.landsat_2009, name='landsat_2009'),
    path('landsat_2010', core_views.landsat_2010, name='landsat_2010'),
    path('landsat_2011', core_views.landsat_2011, name='landsat_2011'),
    path('landsat_2012', core_views.landsat_2012, name='landsat_2012'),
    path('landsat_2013', core_views.landsat_2013, name='landsat_2013'),
    path('landsat_2014', core_views.landsat_2014, name='landsat_2014'),
    path('landsat_2015', core_views.landsat_2015, name='landsat_2015'),
    path('landsat_2016', core_views.landsat_2016, name='landsat_2016'),
    path('landsat_2017', core_views.landsat_2017, name='landsat_2017'),
    path('landsat_2018', core_views.landsat_2018, name='landsat_2018'),
    path('landsat_2019', core_views.landsat_2019, name='landsat_2019'),
    path('landsat_2020', core_views.landsat_2020, name='landsat_2020'),

    path('map/split', core_views.map_split, name='map_split'),
    path('map/my_map', core_views.map_my_map, name='map_my_map'),
]

handler404 = core_views.error_404
handler500 = core_views.error_500

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


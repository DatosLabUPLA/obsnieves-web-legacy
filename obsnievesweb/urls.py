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
    path('visualizadores/lansat/', core_views.display_lansat, name='display_lansat'),
    path('visualizadores/modis/', core_views.display_modis, name='display_modis'),
    path('visualizadores/sentinel/', core_views.display_sentinel, name='display_sentinel'),

    path('noticias/', news_views.news, name='news'),
    path('noticias/<int:pk>', news_views.detail_new, name='detail_new'),


    path('eventos/', core_views.events, name='events'),

    # Modificar para las pruebas del código generado
    path('prueba/', core_views.events, name='events'),

    path('ckeditor/', include('ckeditor_uploader.urls')),
]

handler404 = core_views.error_404
handler500 = core_views.error_500

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


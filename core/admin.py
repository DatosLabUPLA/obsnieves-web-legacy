from django.contrib import admin
from .models import Team, Position

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'id_position')
    search_fields = ('name', 'description')
    ordering = ('-created',)


class PositionAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name',)
    ordering = ('-created',)


admin.site.register(Team, TeamAdmin)
admin.site.register(Position, PositionAdmin)

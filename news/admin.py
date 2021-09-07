from django.contrib import admin
from .models import New, Origin

# Register your models here.
class NewAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('headline', 'date', 'id_origin')
    prepopulated_fields = {"slug": ("headline",)}
    list_filter = ('id_origin__name', 'date')
    search_fields = ('headline', 'date', 'id_origin__name', 'id_origin__short_name')
    ordering = ('-date', 'headline')

class OriginAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'short_name')


admin.site.register(New, NewAdmin)
admin.site.register(Origin, OriginAdmin)

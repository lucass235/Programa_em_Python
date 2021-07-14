from django.contrib import admin
from core.models import Evento

# Register your models here.


class EventoAdmin(admin.ModelAdmin):
    listDisplay = ('titulo', 'dataEvento', 'dataCriacao')
    listFilter = ('titulo', 'dataEvento')


admin.site.register(Evento, EventoAdmin)

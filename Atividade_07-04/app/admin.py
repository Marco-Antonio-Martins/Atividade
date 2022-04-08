from django.contrib import admin
from .models import Pessoa, Evento, EventoCientifico

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    pass

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    pass

@admin.register(EventoCientifico)
class EventoCientificoAdmin(admin.ModelAdmin):
    pass

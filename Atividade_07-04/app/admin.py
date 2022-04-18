from django.contrib import admin
from .models import Evento, EventoCientifico, Autor, PessoaJuridica, PessoaFisica, ArtigoCientifico

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    pass

@admin.register(EventoCientifico)
class EventoCientificoAdmin(admin.ModelAdmin):
    pass

@admin.register(ArtigoCientifico)
class ArtigoCientificoAdmin(admin.ModelAdmin):
    pass

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    pass

@admin.register(PessoaJuridica)
class PessoaJuridicaAdmin(admin.ModelAdmin):
    pass

@admin.register(PessoaFisica)
class PessoaFisicaAdmin(admin.ModelAdmin):
    pass


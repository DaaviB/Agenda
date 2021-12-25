from django.contrib import admin

from .models import Contato, Categoria

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email', 'data_criacao', 'mostrar')
    list_display_links = ('id', 'nome',)
    list_editable = ('telefone', 'email', 'mostrar')
    list_per_page = (10)
    ordering = ('id', 'nome')
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome',)
    list_per_page = (10)


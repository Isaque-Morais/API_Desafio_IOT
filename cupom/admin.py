from django.contrib import admin
from cupom.models import Cupom, ModeloNota

class Cumpons(admin.ModelAdmin):
    list_display = ('id', 'numero_cupom', 'cnpj','cpf_doador', 'data', 'valor_compra', 'entidade_doacao')
    list_display_links = ('id', 'numero_cupom')
    search_fields = ('nome',)
    list_per_page = 20
    
admin.site.register(Cupom, Cumpons)

class ModelosCupons(admin.ModelAdmin):
    list_display = ('id', 'codigo_nota', 'descricao')
    list_display_likns = ('id', 'codigo_curso')
    search_fields = ('codigo_curso',)
    
admin.site.register(ModeloNota, ModelosCupons)
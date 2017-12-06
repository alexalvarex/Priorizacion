from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Sexo)
admin.site.register(Pais)
admin.site.register(Depto)
admin.site.register(Municipio)

# DSC Priorizacion de comunidades
admin.site.register(Comunidad)
admin.site.register(Mapa)
admin.site.register(Lote)
admin.site.register(Criterio)
admin.site.register(Tenencia)
admin.site.register(Zona)
admin.site.register(EstadoFinca)
admin.site.register(SistemaCosecha)
admin.site.register(Finca)
admin.site.register(TipoComunidad)
admin.site.register(AbasAgua)
admin.site.register(Descicion)
admin.site.register(Priorizar)
admin.site.register(Capa)
admin.site.register(Resultados)
admin.site.register(TipoQuema)

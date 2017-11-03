from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Sexo)
admin.site.register(Pais)
admin.site.register(Depto)
admin.site.register(Municipio)
admin.site.register(Residencia)
admin.site.register(TipoSangre)
admin.site.register(EstadoVida)
admin.site.register(EstadoCivil)
admin.site.register(NivelAcademico)
admin.site.register(GradosEducativos)
admin.site.register(GradosCursados)
admin.site.register(TipoUsuario)
admin.site.register(TipoParentezco)
admin.site.register(Personas)
admin.site.register(Colaborador)
admin.site.register(Beneficiarios)
admin.site.register(FamiliaLaborando)
admin.site.register(FamiliaColaborador)

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

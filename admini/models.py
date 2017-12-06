from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.utils import timezone
now = timezone.now()

# BENEFICIOS DE LOS COLABORADORES
@python_2_unicode_compatible
class Sexo(models.Model):
	sexo = models.CharField(max_length=9)

	def __str__(self):
		return self.sexo

@python_2_unicode_compatible
class Pais(models.Model):
	pais = models.CharField(max_length=50)

	def __str__(self):
		return self.pais

@python_2_unicode_compatible
class Depto(models.Model):
	depto = models.CharField(max_length=50)
	pais = models.ForeignKey(Pais)

	def __str__(self):
		return self.depto

@python_2_unicode_compatible
class Municipio(models.Model):
	municipio = models.CharField(max_length=50)
	depto = models.ForeignKey(Depto)

	def __str__(self):
		return self.municipio

@python_2_unicode_compatible
class Residencia(models.Model):
	residencia = models.CharField(max_length=50)
	municipio = models.ForeignKey(Municipio)

	def __str__(self):
		return self.municipio


class TipoSangre(models.Model):
	tipo_sangre = models.CharField(max_length=10)

	def __str__(self):
		return self.tipo_sangre


class EstadoVida(models.Model):
	estado_vida = models.CharField(max_length=10)

	def __str__(self):
		return self.estado_vida


class EstadoCivil(models.Model):
	estado_civil = models.CharField(max_length=30)

	def __str__(self):
		return self.estado_civil


class NivelAcademico(models.Model):
	nivel_academico = models.CharField(max_length=50)

	def __str__(self):
		return self.nivel_academico


class GradosEducativos(models.Model):
	grados_educativos = models.CharField(max_length=50)

	def __str__(self):
		return self.grados_educativos

class GradosCursados(models.Model):
	grados_educativos = models.ForeignKey(GradosEducativos)
	nivel_academico = models.ForeignKey(NivelAcademico)

	def __str__(self):
		return "%s %s" %(self.grados_educativos, self.nivel_academico)

class TipoUsuario(models.Model):
	tipo_usuario = models.CharField(max_length=50)

	def __str__(self):
		return self.tipo_usuario


class TipoParentezco(models.Model):
	tipo_parentezco = models.CharField(max_length=50)

	def __str__(self):
		return self.tipo_parentezco

@python_2_unicode_compatible
class Personas(models.Model):
	numid = models.CharField(max_length=15)	
	nombre = models.CharField(max_length=50)	
	apellido = models.CharField(max_length=50)	
	direccion = models.CharField(max_length=100)
	telefono_f = models.CharField(max_length=9, blank=True, null=True)
	telefono_c = models.CharField(max_length=9, blank=True, null=True)
	correo = models.EmailField(blank=True, null=True)
	sexo = models.ForeignKey(Sexo)
	residencia = models.ForeignKey(Residencia)
	tipo_sangre = models.ForeignKey(TipoSangre)
	estado_civil = models.ForeignKey(EstadoCivil)
	grados_cursados = models.ForeignKey(GradosCursados)
	

	def __str__(self):
		return "%s %s" %(self.nombre, self.apellido)

@python_2_unicode_compatible
class UnidadOrganizativa(models.Model):
	unidad_organizativa = models.CharField(max_length=100)

	def __str__(self):
		return self.unidad_organizativa

@python_2_unicode_compatible
class Colaborador(models.Model):
	codigo = models.CharField(max_length=50)
	unidad_organizativa = models.ForeignKey(UnidadOrganizativa)
	persona = models.ForeignKey(Personas, related_name='Persona')
	persona_refirio =  models.ForeignKey(Personas, related_name='PersonaReferida')
	usuario = models.OneToOneField(User, related_name='Persona')
	fechac_ingreso  = models.DateTimeField()

	def __str__(self):
		return "%s %s" %(self.persona.nombre, self.persona.apellido)

@python_2_unicode_compatible
class Beneficiarios(models.Model):
	persona = models.ManyToManyField(Personas)
	colaborador = models.OneToOneField(Colaborador)
	porcentaje = models.IntegerField()

	def __str__(self):
		return "%s %s" %(self.persona.nombre, self.persona.apellido)

@python_2_unicode_compatible
class FamiliaLaborando(models.Model):
	persona = models.ManyToManyField(Personas)
	colaborador = models.OneToOneField(Colaborador)

	def __str__(self):
		return "%s %s" %(self.persona.nombre, self.persona.apellido)

@python_2_unicode_compatible
class FamiliaColaborador(models.Model):
	persona = models.ManyToManyField(Personas)
	colaborador = models.OneToOneField(Colaborador)

	def __str__(self):
		return "%s %s" %(self.persona.nombre, self.persona.apellido)

# DSC PRIORIZACION DE COMUNIDADES

@python_2_unicode_compatible
class Descicion(models.Model):
	des = models.CharField(max_length=9)

	def __str__(self):
		return self.des

@python_2_unicode_compatible
class TipoComunidad(models.Model):
	tipo = models.CharField(max_length=100)

	def __str__(self):
		return self.tipo

@python_2_unicode_compatible
class AbasAgua(models.Model):
	agua = models.CharField(max_length=100)

	def __str__(self):
		return self.agua

@python_2_unicode_compatible
class TipoQuema(models.Model):
	tipo_quema = models.CharField(max_length=100)

	def __str__(self):
		return self.tipo_quema

@python_2_unicode_compatible
class Comunidad(models.Model):
	nombre = models.CharField(max_length=100)
	municipio = models.ForeignKey(Municipio, related_name='Municipio')
	codigo = models.IntegerField(blank=True, null=True)
	cant_m = models.IntegerField(blank=True, null=True)
	cant_h = models.IntegerField(blank=True, null=True)
	cant_c = models.IntegerField(blank=True, null=True)
	tipo_comunidad = models.ForeignKey(TipoComunidad, related_name='Tipo_Comunidad')
	procedencia = models.ForeignKey(Descicion, related_name='Procedencia')
	agua = models.ManyToManyField(AbasAgua, related_name='Abastecimiento_Agua')
	toneladas = models.FloatField(blank=True, null=True)
	tipo_quema = models.ForeignKey(TipoQuema, default=3)
	ha = models.IntegerField(blank=True, null=True, default=0)
	ton_ha = models.IntegerField(blank=True, null=True, default=0)
	ton_total = models.FloatField(blank=True, null=True, default=0)
	pi = models.ForeignKey(Descicion, related_name='Productores')

	def __str__(self):
		return "%s - %s" %(self.nombre, self.municipio)

@python_2_unicode_compatible
class Mapa(models.Model):
	comunidadInicio = models.ForeignKey(Comunidad, related_name='Comunidad_Inicio')
	comunidadFinal = models.ForeignKey(Comunidad, related_name='Comunidad_Final')

	def __str__(self):
		return "%s - %s" %(self.comunidadInicio, self.comunidadFinal)


class Lote(models.Model):
	codLote = models.IntegerField()
	comunidad = models.ManyToManyField(Comunidad)

	def __unicode__(self):
		return str(self.codLote)

@python_2_unicode_compatible
class Criterio(models.Model):
	criterio = models.CharField(max_length=100)

	def __str__(self):
		return self.criterio

@python_2_unicode_compatible
class Tenencia(models.Model):
	tenencia = models.CharField(max_length=100)

	def __str__(self):
		return self.tenencia

@python_2_unicode_compatible
class Zona(models.Model):
	zona = models.CharField(max_length=10)

	def __str__(self):
		return self.zona

@python_2_unicode_compatible
class EstadoFinca(models.Model):
	estado = models.CharField(max_length=100)

	def __str__(self):
		return self.estado

@python_2_unicode_compatible
class SistemaCosecha(models.Model):
	sistemaCosecha = models.CharField(max_length=100)

	def __str__(self):
		return self.sistemaCosecha

@python_2_unicode_compatible
class Finca(models.Model):
	tenencia = models.ForeignKey(Tenencia, related_name='Tenencia')
	hnton = models.FloatField(blank=True, null=True)
	zona = models.ForeignKey(Zona, related_name='Zona_o_Distrito')
	codFinca = models.CharField(max_length=10)
	nombre = models.CharField(max_length=100)
	lote = models.ForeignKey(Lote)
	toneladasReales = models.FloatField()
	distancia = models.FloatField()
	comunidad = models.ForeignKey(Comunidad)
	estado = models.ForeignKey(EstadoFinca)
	sistemaCosecha = models.ForeignKey(SistemaCosecha)

	def _fincaLote(self):
		return "%s%s" %(self.codFinca, self.lote)

	fincaLote = property(_fincaLote)

	def __str__(self):
		return "%s %s" %(self.codFinca, self.nombre)

@python_2_unicode_compatible
class Capa(models.Model):
	zafra = models.CharField(max_length=100)
	inicio = models.DateField(blank=True, null=True)
	fin = models.DateField(blank=True, null=True)

	def __str__(self):
		return "%s" %(self.zafra)

@python_2_unicode_compatible
class Priorizar(models.Model):
	valoragua = models.IntegerField(null=True)
	valorruta = models.IntegerField(null=True)
	valortone = models.IntegerField(null=True)
	valorproce = models.IntegerField(null=True)
	valorqmi = models.IntegerField(null=True)
	valorpi = models.IntegerField(null=True)
	capa = models.ForeignKey(Capa)
	comunidad = models.ManyToManyField(Comunidad)

	def __str__(self):
		return "%s" %(self.capa)

@python_2_unicode_compatible
class Resultados(models.Model):
	comunidad = models.ForeignKey(Comunidad)
	total = models.FloatField(blank=True, null=True)
	criterios = models.ForeignKey(Priorizar)

	def __str__(self):
		return "%s - %s %s" %(self.comunidad, self.total, '%')

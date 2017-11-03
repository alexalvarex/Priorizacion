from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from .models import *
from django.db.models import Count
from django.db.models import Max


from django.contrib.auth.models import User

# Create your views here.
def index(request):
	return render(request, 'index.html')

def all_user(request):
	data = User.objects.all()
	perfil = Personas.objects.all()
	sexo = Sexo.objects.all()
	numu = data.count()
	return render(request, 'all_users.html', {'data':data,'perfil': perfil, 'numu':numu, 'sexo':sexo})

def all_employees(request):
	colaboradores = Colaborador.objects.all()
	numc = colaboradores.count()
	municipio = Municipio.objects.all()
	return render(request, 'all_employees.html', {'data':colaboradores, 'numc':numc, 'muni': municipio})

def new_user(request):
	sexo = Sexo.objects.all()
	return render(request, 'new_user.html', {'sexo': sexo})

def new_user_add(request):
	if request.method == 'POST':
		try:
			numid = request.POST.get('numid')
			nombre = request.POST.get('nombre')
			apellido = request.POST.get('apellido')
			fijo = request.POST.get('telefono')
			cel = request.POST.get('celular')
			correo = request.POST.get('correo')
			sex =  request.POST.get('sexo')
			sexo = Sexo.objects.get(pk = sex)
			username = request.POST.get('username')
			contra = request.POST.get('contra')
			codigo = request.POST.get('codigo')

			us = User.objects.create(
					username = username, 
					password = contra, 
					first_name = nombre, 
					last_name = apellido,
					email = correo
				)
			perfil = beneficios_perfil(
					numid = numid, 
					direccion = direccion, 
					telefono_f = fijo, 
					telefono_c = cel, 
					usuario = us, 
					sexo = sexo)
			perfil.save()
			return HttpResponseRedirect('/principal/usuarios/new/')
		except Exception as e:
			return HttpResponse(e)

def all_comunidades(request):
	comunidad = Comunidad.objects.all()
	numc = comunidad.count()
	municipio = Municipio.objects.all()
	return render(request, 'all_comunidades.html', {'data':comunidad, 'numc':numc, 'muni': municipio})

def new_comunidad(request):
	# cholu = Depto.objects.get(pk = 1)
	# valle = Depto.objects.get(pk = 2)
	municholu = Municipio.objects.filter(depto = 1)
	munivalle = Municipio.objects.filter(depto = 2)
	tipoc = TipoComunidad.objects.all()
	agua = AbasAgua.objects.all()
	des = Descicion.objects.all()
	return render(request, 'new_comunidad.html', {'municholu': municholu, 'munivalle':munivalle,'tipoc':tipoc, 'agua':agua, 'des':des})

def new_comunidad_add(request):
	if request.method == 'POST':
		try:
			nombre = request.POST.get('nombre')
			muni = request.POST.get('muni')
			tipoc = request.POST.get('tipoc')
			cant_m = request.POST.get('cant_m')
			cant_h = request.POST.get('cant_h')
			des = request.POST.get('des')
			nombree = request.POST.get('nombree')
			agua = request.POST.get('agua')

			municipio = Municipio.objects.get(pk = muni)
			tipoco = TipoComunidad.objects.get(pk = tipoc)
			escuela = Descicion.objects.get(pk = des)
			abas = AbasAgua.objects.get(pk = agua)

			comunidad = Comunidad(
					nombre = nombre, 
					municipio = municipio,
					cant_h = cant_h,
					cant_m = cant_m,
					tipo_comunidad = tipoco,
					des = escuela,
					escuela = nombree,
					agua = abas)
			comunidad.save()
			return HttpResponseRedirect('/principal/comunidad/new/')
		except Exception as e:
			return HttpResponse(e)

def fincasxco(request, pk):
	comunidad = Comunidad.objects.get(pk = pk)
	fincas = Finca.objects.filter(comunidad = pk)
	return render(request, 'fincasxco.html', {'data':fincas, 'comunidad':comunidad})

def priorizar(request, pk):
	criterios = Criterio.objects.all()
	comunidad = Comunidad.objects.get(pk=pk)
	distancia = Finca.objects.all()
	mayor = distancia.aggregate(Max('distancia'))
	return render(request, 'priorizar.html', {'comunidad':comunidad, 'criterios': criterios, 'mayor': mayor})

def priorizar_add(request):
	if request.method == 'POST':
		try:
			alumnos = request.POST.getlist('alumno[]')
			grado = request.POST.get('grado')
			centro = request.POST.get('centro')
			primer = request.POST.get('primer')
			horario = request.POST.get('horario')
			fechai = request.POST.get('fechai')
			fechaf = request.POST.get('fechaf')
			# archivos = request.FILES['archivos']

			g = Grado.objects.get(pk=grado)
			c = Centro.objects.get(pk = centro)
			d = Periodo.objects.get(pk=primer)
			for alumno in alumnos:	
				a = Personas.objects.get(pk=alumno)
				mat = Matricula(fecha = datetime.now() , persona = a, centro = c, grado = g, 
					num_periodo = d, horario = horario, 
					inicio_clases = fechai, fin_clases = fechaf)	
				mat.save()
			return HttpResponseRedirect('/principal/enroll/new/')
		except Exception as e:
			return HttpResponse(e)
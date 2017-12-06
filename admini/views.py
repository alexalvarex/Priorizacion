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


@login_required()
def index(request):
	return render(request, 'index.html')

@login_required()
def all_user(request):
	data = User.objects.all()
	perfil = Personas.objects.all()
	sexo = Sexo.objects.all()
	numu = data.count()
	return render(request, 'all_users.html', {'data':data,'perfil': perfil, 'numu':numu, 'sexo':sexo})

@login_required()
def all_employees(request):
	colaboradores = Colaborador.objects.all()
	numc = colaboradores.count()
	municipio = Municipio.objects.all()
	return render(request, 'all_employees.html', {'data':colaboradores, 'numc':numc, 'muni': municipio})

@login_required()
def new_user(request):
	sexo = Sexo.objects.all()
	return render(request, 'new_user.html', {'sexo': sexo})

@login_required()
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

@login_required()
def all_comunidades(request):
	departamentos = Depto.objects.all()
	return render(request, 'comunidades_cat.html', {'data':departamentos})

@login_required()
def comunidadesxdepto(request, pk):
	depto = Depto.objects.get(pk = pk)

	lista_cholu = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
	lista_valle = [17,18,19,20,21,22,23,24,25]
	comunidades = Comunidad.objects.all()
 	comunidades_cholu = comunidades.exclude(municipio__in=lista_valle)
 	comunidades_valle = comunidades.exclude(municipio__in=lista_cholu)
 	comu = Comunidad.objects.get(pk = 60)
	agua = comu.agua.all()

	numc = comunidades_cholu.count()
	numv = comunidades_valle.count()
	return render(request, 'comunidadesxdepto.html',{'comunidades_cholu':comunidades_cholu, 'comunidades_valle':comunidades_valle, 
			'numc':numc, 'numv':numv, 'depto': depto, 'agua':agua})

@login_required()
def new_comunidad(request):
	municholu = Municipio.objects.filter(depto = 1)
	munivalle = Municipio.objects.filter(depto = 2)
	tipoc = TipoComunidad.objects.all()
	agua = AbasAgua.objects.all()
	des = Descicion.objects.all()
	quemas = TipoQuema.objects.all()
	return render(request, 'new_comunidad.html', {'municholu': municholu, 
		'munivalle':munivalle,'tipoc':tipoc, 'agua':agua, 'des':des, 'quemas':quemas})

@login_required()
def new_comunidad_add(request):
	if request.method == 'POST':
		try:
			nombre = request.POST.get('nombre')
			muni = request.POST.get('muni')
			tipoc = request.POST.get('tipoc')
			cant_m = request.POST.get('cant_m')
			cant_h = request.POST.get('cant_h')
			cant_c = request.POST.get('cant_c')
			proce = request.POST.get('proce')
			codigo = request.POST.get('codigo')
			toneladas = request.POST.get('toneladas')
			tipo_quema = request.POST.get('tipo_quema')
			ha = request.POST.get('ha')
			ton_ha = request.POST.get('ton_ha')
			pi = request.POST.get('pi')
			agua = request.POST.getlist('agua[]')

			municipio = Municipio.objects.get(pk = muni)
			tipoco = TipoComunidad.objects.get(pk = tipoc)
			procedencia = Descicion.objects.get(pk = proce)
			productores = Descicion.objects.get(pk = pi)
			tq = TipoQuema.objects.get(pk=tipo_quema)

			ton_total = int(ha) * int(ton_ha)

			comunidad = Comunidad(
					nombre = nombre, 
					municipio = municipio,
					codigo = codigo,
					cant_m = cant_m,
					cant_h = cant_h,
					cant_c = cant_c,
					tipo_comunidad = tipoco,
					procedencia = procedencia,
					toneladas = toneladas,
					tipo_quema = tq,
					ha = ha,
					ton_ha = ton_ha,
					ton_total = ton_total,
					pi = productores)
			comunidad.save()

			for a in agua:
				abas = AbasAgua.objects.get(pk = a)
				comunidad.agua.add(abas)

			return HttpResponseRedirect('/principal/comunidades/new/')
		except Exception as e:
			return HttpResponse(e)

@login_required()
def editar_comunidad(request, pk):
	municholu = Municipio.objects.filter(depto = 1)
	munivalle = Municipio.objects.filter(depto = 2)
	tipoc = TipoComunidad.objects.all()
	agua = AbasAgua.objects.all()
	des = Descicion.objects.all()
	comunidad = Comunidad.objects.get(pk = pk)
	quemas = TipoQuema.objects.all()
	return render(request, 'editar_comunidad.html', {'municholu': municholu, 'quemas':quemas,
		'munivalle':munivalle,'tipoc':tipoc, 'agua':agua, 'des':des, 'comunidad':comunidad})

@login_required()
def editar_comunidad_add(request):
	if request.method == 'POST':
		try:
			nombre = request.POST.get('nombre')
			pk = request.POST.get('id')
			muni = request.POST.get('muni')
			tipoc = request.POST.get('tipoc')
			cant_m = request.POST.get('cant_m')
			cant_h = request.POST.get('cant_h')
			cant_c = request.POST.get('cant_c')
			proce = request.POST.get('proce')
			codigo = request.POST.get('codigo')
			toneladas = request.POST.get('toneladas')
			agua = request.POST.getlist('agua[]')
			tipo_quema = request.POST.get('tipo_quema')
			ha = request.POST.get('ha')
			ton_ha = request.POST.get('ton_ha')
			pi = request.POST.get('pi')

			municipio = Municipio.objects.get(pk = muni)
			tipoco = TipoComunidad.objects.get(pk = tipoc)
			procedencia = Descicion.objects.get(pk = proce)
			productores = Descicion.objects.get(pk = pi)
			tq = TipoQuema.objects.get(pk=tipo_quema)

			ton_total = int(ha) * int(ton_ha)

			comunidad = Comunidad.objects.get(pk = pk)
			comunidad.nombre = nombre 
			comunidad.municipio = municipio
			comunidad.codigo = codigo
			comunidad.cant_m = cant_m
			comunidad.cant_h = cant_h
			comunidad.cant_c = cant_c
			comunidad.tipo_comunidad = tipoco
			comunidad.procedencia = procedencia
			toneladas = toneladas
			comunidad.tipo_quema = tq
			comunidad.ha = ha
			comunidad.ton_ha = ton_ha
			comunidad.ton_total = ton_total
			comunidad.pi = productores
			comunidad.save()

			for a in agua:
				abas = AbasAgua.objects.get(pk = a)
				comunidad.agua.add(abas)

			return HttpResponseRedirect(reverse('comunidadesxdepto', args=[comunidad.municipio.depto.id]))
		except Exception as e:
			return HttpResponse(e)

@login_required()
def fincasxco(request, pk):
	comunidad = Comunidad.objects.get(pk = pk)
	fincas = Finca.objects.filter(comunidad = pk)
	numf = fincas.count()
	return render(request, 'fincasxco.html', {'data':fincas, 'comunidad':comunidad, 'numf':numf})

@login_required()
def priorizar(request):
	criterios = Criterio.objects.all()
	distancia = Finca.objects.all()
	mayor = distancia.aggregate(Max('distancia'))
	priorizar = Priorizar.objects.all()
	comu = Comunidad.objects.all()
	return render(request, 'priorizar.html', {'criterios': criterios, 'comu': comu})

@login_required()
def priorizar_add(request):
	if request.method == 'POST':
		try:
			valoragua = request.POST.get('valoragua')
			valorruta = request.POST.get('valorruta')
			valortone = request.POST.get('valortone')
			valorproce = request.POST.get('valorproce')
			valorqmi = request.POST.get('valorqmi')
			valorpi = request.POST.get('valorpi')
			total = request.POST.get('total')
			comu = request.POST.getlist('comu[]')

			capa = Capa.objects.latest('id')
			
			prio = Priorizar(
							valoragua = valoragua,
							valorruta = valorruta,
							valortone = valortone,
							valorproce = valorproce,
							valorqmi = valorqmi,
							valorpi = valorpi,	
							capa = capa)	
			prio.save()

			ruta_rodea = TipoComunidad.objects.get(pk = 1)
			ruta_atraviesa = TipoComunidad.objects.get(pk = 2)
			si = Descicion.objects.get(pk = 1)
			no = Descicion.objects.get(pk = 2)

			for c in comu:
				comu = Comunidad.objects.get(pk = c)
				prio.comunidad.add(comu)
				resultado = Resultados(
					comunidad = comu,
					criterios = prio
				) 
				resultado.save()
				agua = int(prio.valoragua)
				ruta = int(prio.valorruta)
				tone = int(prio.valortone)
				proce = int(prio.valorproce)
				qmi = int(prio.valorqmi)
				pi = int(prio.valorpi)
				media_ruta = int(prio.valorruta) / 2
				# ton_total = int(resultado.comunidad.ha) * int(resultado.comunidad.ton_ha)

				cant_agua = comu.agua.all().count()
				if resultado.comunidad.tipo_comunidad == ruta_atraviesa:
					resultado.total = ruta
					resultado.save()
				if resultado.comunidad.tipo_comunidad == ruta_rodea:
					resultado.total = media_ruta
					resultado.save()
				if cant_agua >= 3:
					resultado.total = int(resultado.total) + int(agua)
					resultado.save()
				if cant_agua <= 2:
					resultado.total = resultado.total + (agua * 0.5)
					resultado.save()
				if resultado.comunidad.toneladas > 50000:
					resultado.total = int(resultado.total) + tone
					resultado.save()
				if resultado.comunidad.toneladas <= 50000:
					resultado.total = int(resultado.total) + (tone * 0.5)
					resultado.save()
				if resultado.comunidad.procedencia == si:
					resultado.total = int(resultado.total) + proce
					resultado.save()
				if resultado.comunidad.procedencia == no:
					resultado.total = int(resultado.total) + (proce * 0.5)
					resultado.save()
				if resultado.comunidad.ton_total > 0:
					resultado.total = int(resultado.total) + qmi
					resultado.save()
				if resultado.comunidad.ton_total == 0:
					resultado.total = int(resultado.total) + (qmi * 0.5)
					resultado.save()
				if resultado.comunidad.pi == no:
					resultado.total = int(resultado.total) + (pi * 0.5)
					resultado.save()
				if resultado.comunidad.pi == si:
					resultado.total = int(resultado.total) + pi
					resultado.save()


			return HttpResponseRedirect('/principal/priorizar/')
		except Exception as e:
			return HttpResponse(e)

@login_required()
def comunidades_priorizadas(request, pk):
	# priorizar = Priorizar.objects.all()
	capa = Capa.objects.get(pk = pk)
	priorizar = Priorizar.objects.filter(capa = capa)
	nump = priorizar.count()
	return render(request, 'priorizar_cat.html', {'priorizar': priorizar, 'nump':nump})

@login_required()
def priorizar_graficos(request):
 	sobresaliente = Resultados.objects.filter(total__range=(91, 100))
 	numso = sobresaliente.count()
 	muybueno = Resultados.objects.filter(total__range=(81, 90))
 	nummb = muybueno.count()
 	bueno = Resultados.objects.filter(total__range=(71, 80))
 	numb = bueno.count()
 	bronce = Resultados.objects.filter(total__range=(0, 70))
 	numbronce = bronce.count()
	return render(request, 'graficos.html', {'sobresaliente': sobresaliente, 'muybueno': muybueno, 
		'bueno': bueno, 'bronce':bronce, 'numbronce':numbronce, 'numso': numso, 'nummb': nummb, 'numb': numb,
		'numbronce':numbronce})

@login_required()
def capa(request):
	capa = Capa.objects.all()
	numc = capa.count()
	return render(request, 'capa.html', {'capa':capa, 'numc': numc})

@login_required()
def capa_add(request):
	if request.method == 'POST':
		try:
			zafra = request.POST.get('zafra')
			fechai = request.POST.get('fechai')
			fechaf = request.POST.get('fechaf')

			c = Capa(
				zafra = zafra,
				inicio = fechai,
				fin = fechaf
				)
			c.save()

			return HttpResponseRedirect(reverse('capa'))
		except Exception as e:
			return HttpResponse(e)


@login_required()
def capa_comunidad(request):
	capa = Priorizar.objects.all()
	return render(request, 'capa_comunidad.html', {'capa':capa})

@login_required()
def comu_delete(request, pk):
	comu = Comunidad.objects.get(pk = pk)
	try:
		comu.delete()
		return HttpResponseRedirect(reverse('comunidadesxdepto', args=[comu.municipio.depto.id]))
	except Exception, e:
		return HttpResponse(e)
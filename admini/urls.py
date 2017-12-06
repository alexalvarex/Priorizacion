from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^usuarios/$', views.all_user, name='all_users'),
	url(r'^usuarios/new/$', views.new_user, name='new_user'),
	url(r'^usuarios/new/add/$', views.new_user_add, name='new_user_add'),
	url(r'^employees/$', views.all_employees, name='all_employees'),
	url(r'^comunidades/$', views.all_comunidades, name='all_comunidades'),
	url(r'^comunidades/depto/(?P<pk>\d+)/$', views.comunidadesxdepto, name='comunidadesxdepto'),
	url(r'^comunidades/new/$', views.new_comunidad, name='new_comunidad'),
	url(r'^comunidades/new/add/$', views.new_comunidad_add, name='new_comunidad_add'),
	url(r'^comunidades/fincas/(?P<pk>\d+)/$', views.fincasxco, name='fincasxco'),
	url(r'^priorizar/$', views.priorizar, name='priorizar'),
	url(r'^priorizar/add/$', views.priorizar_add, name='priorizar_add'),
	url(r'^comunidades/priorizadas/(?P<pk>\d+)/$', views.comunidades_priorizadas, name='comunidades_priorizadas'),
	url(r'^priorizar/graficos/$', views.priorizar_graficos, name='priorizar_graficos'),
	url(r'^configuracion/$', views.capa, name='capa'),
	url(r'^configuracion/add/$', views.capa_add, name='capa_add'),
	url(r'^comunidades/capas/$', views.capa_comunidad, name='capa_comunidad'),
	url(r'^comunidades/editar/(?P<pk>\d+)/$', views.editar_comunidad, name='editar_comunidad'),
	url(r'^comunidades/editar/add/$', views.editar_comunidad_add, name='editar_comunidad_add'),
	url(r'^comunidad/delete/(?P<pk>\d+)/$', views.comu_delete, name='comu_delete'),

]
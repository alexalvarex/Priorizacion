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
	url(r'^comunidades/new/$', views.new_comunidad, name='new_comunidad'),
	url(r'^comunidades/new/add/$', views.new_comunidad_add, name='new_comunidad_add'),
	url(r'^comunidades/fincas/(?P<pk>\d+)/$', views.fincasxco, name='fincasxco'),
	url(r'^priorizar/(?P<pk>\d+)/$', views.priorizar, name='priorizar'),
	url(r'^priorizar/(?P<pk>\d+)/add/$', views.priorizar_add, name='priorizar_add'),

]
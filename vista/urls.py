# -*- coding: utf-8 -*-

from django.conf.urls import url
from vista import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'configuracion', views.configuracion, name='configuracion'),
    url(r'nodos/agregar', views.add_nodo, name='add_nodo'),
    url(r'nodos/borrar/(?P<id>[0-9]+)', views.del_nodo, name='del_nodo'),
    url(r'nodos/editar/(?P<id>[0-9]+)', views.edit_nodo, name='edit_nodo'),
    url(r'nodos/mostrar/(?P<id>[0-9]+)', views.show_nodo, name='show_nodo'),
    url(r'nodos', views.nodos, name='nodos'),
    #url(r'evento/show_evento/(?P<id>[0-9]+)', views.show_evento, name='show_evento'),
    url(r'evento', views.evento, name='evento'),

    url(r'alarma/add_alarma', views.add_alarma, name='add_alarma'),
    url(r'alarma/mostrar/(?P<id>[0-9]+)', views.show_alarma, name='show_alarma'),
    url(r'alarma/editar/(?P<id>[0-9]+)', views.edit_alarma, name='edit_alarma'),
    url(r'alarma/borrar/(?P<id>[0-9]+)', views.del_alarma, name='del_alarma'),
    url(r'alarma', views.alarma, name='alarma'),



]

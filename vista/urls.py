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
    url(r'nodos', views.nodos, name='nodos')
]

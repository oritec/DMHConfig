# -*- coding: utf-8 -*-
from django.shortcuts import render
from vista.functions import *
from models import NodeStatus, NodeConfig, FlowSources
from forms import NodeConfigForm
import logging
logger = logging.getLogger('oritec')
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def index(request):
    contenido=ContenidoContainer()
    contenido.user=request.user
    contenido.titulo=u'Flujometros DMH'
    contenido.subtitulo=u'Status del sistema'
    contenido.menu = ['menu-principal', 'menu2-status']

    nodos = NodeStatus.objects.all()

    return render(request, 'vista/index.html',
        {'cont': contenido,
         'nodos': nodos
        })

def configuracion(request):
    contenido = ContenidoContainer()
    contenido.user = request.user
    contenido.titulo = u'Flujometros DMH'
    contenido.subtitulo = u'Configuración del sistema'
    contenido.menu = ['menu-principal', 'menu2-configuracion']

    sources = FlowSources.objects.all()

    return render(request, 'vista/configuracion.html',
                  {'cont': contenido,
                   'sources': sources
                   })

def nodos(request):
    contenido = ContenidoContainer()
    contenido.user = request.user
    contenido.titulo = u'Flujometros DMH'
    contenido.subtitulo = u'Configuración de nodos'
    contenido.menu = ['menu-principal', 'menu2-nodos']

    configs = NodeConfig.objects.all()

    return render(request, 'vista/nodos.html',
                  {'cont': contenido,
                   'configs': configs
                   })

def add_nodo(request):
    contenido = ContenidoContainer()
    contenido.user = request.user
    contenido.titulo = u'Flujometros DMH'
    contenido.subtitulo = u'Agregar configuración'
    contenido.menu = ['menu-principal', 'menu2-nodos']

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NodeConfigForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            nodo = form.save()
            nodo_status = NodeStatus.objects.get(nodeId=nodo.nodeId)
            nodo_status.hasConfig = True
            nodo_status.save()
            return HttpResponseRedirect('/nodos')

            # if a GET (or any other method) we'll create a blank form
    else:
        logger.debug(request.GET.get('nodo', None))
        nodo = request.GET.get('nodo', None)
        flow = FlowSources.objects.get(id=1)
        if nodo is not None:
            form = NodeConfigForm(initial={'nodeId':nodo,'flowSource':flow.id})
        else:
            form = NodeConfigForm(initial={'flowSource':flow.id})

    return render(request, 'vista/addNode.html',
                  {'cont': contenido,
                   'form': form
                   })

def edit_nodo(request,id):
    contenido = ContenidoContainer()
    contenido.user = request.user
    contenido.titulo = u'Flujometros DMH'
    contenido.subtitulo = u'Editar configuración'
    contenido.menu = ['menu-principal', 'menu2-nodos']

    conf = NodeConfig.objects.get(nodeId = id)

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NodeConfigForm(request.POST,instance=conf)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return HttpResponseRedirect(reverse('vista:nodos'))

            # if a GET (or any other method) we'll create a blank form
    else:
        form = NodeConfigForm(instance=conf)

    return render(request, 'vista/addNode.html',
                  {'cont': contenido,
                   'form': form,
                   'nodeId': conf.nodeId
                   })

def del_nodo(request,id):
    if request.method == 'POST':
        conf = NodeConfig.objects.get(nodeId=id)
        nodo_status = NodeStatus.objects.get(nodeId=conf.nodeId)
        nodo_status.hasConfig = False
        nodo_status.save()
        conf.delete()
    return HttpResponseRedirect(reverse('vista:nodos'))

def show_nodo(request,id):
    contenido = ContenidoContainer()
    contenido.user = request.user
    contenido.titulo = u'Flujometros DMH'
    contenido.subtitulo = u'Mostrar configuración'
    contenido.menu = ['menu-principal', 'menu2-nodos']

    conf = NodeConfig.objects.get(nodeId = id)

    form = NodeConfigForm(instance=conf)

    return render(request, 'vista/showNode.html',
                  {'cont': contenido,
                   'form': form,
                   'nodeId': conf.nodeId
                   })
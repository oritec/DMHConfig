# -*- coding: utf-8 -*-
from django.shortcuts import render
from vista.functions import *
from models import NodeStatus, NodeConfig, FlowSources, SystemConfig
from models import Eventos, Alarma
from forms import NodeConfigForm, EventoForm, AlarmaForm, SystemConfigForm
from django.contrib import messages



import logging
logger = logging.getLogger('oritec')
from django.http import HttpResponseRedirect, HttpResponse

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

    form = None
    instancia = SystemConfig.objects.get(id=1)

    sources = FlowSources.objects.all()

    if request.method == 'POST':
        form = SystemConfigForm(request.POST, instance=instancia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Configuración guardada con éxito!')
        else:
            messages.error(request,'Error en la configuración')

    if form is None:
        form = SystemConfigForm(instance=instancia)

    return render(request, 'vista/configuracion.html',
                  {'cont': contenido,
                   'sources': sources,
                   'form': form,
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

def evento(request):
    contenido = ContenidoContainer()
    contenido.user = request.user
    contenido.titulo = u'Eventos DMH'
    contenido.subtitulo = u'Mostrar eventos'
    contenido.menu = ['menu-principal', 'menu2-evento']

    #datos = Eventos.objects.all()
    # Los datos se ordenan por el campo 'inicio' que corresponde a la fecha de inicio
    # el "-" indica que se hace un orden de la fecha actual a la mas antigua
    # el ":[int]" indica que se devuelven los n primeros/ultimos registros, en este caso n=10
    datos = Eventos.objects.all().order_by('-inicio')[:10]


    return render(request, 'vista/evento.html',
                  {'cont': contenido,
                   'data': datos,
                   })

def show_evento(request,id):
    contenido = ContenidoContainer()
    contenido.user = request.user
    contenido.titulo = u'Eventos DMH'
    contenido.subtitulo = u'Mostrar detalle evento'
    contenido.menu = ['menu-principal', 'menu2-evento']

    conf = Eventos.objects.get(id = id)
    form = EventoForm(instance=conf)

    return render(request, 'vista/evento_detalle.html',
                  {'cont': contenido,
                   'form': form,
                   'id': conf.id
                   })

# *******************************************************************************

def add_alarma(request):
    contenido = ContenidoContainer()
    contenido.user = request.user
    contenido.titulo = u'Alarmas DMH'
    contenido.subtitulo = u'Agregar Alarma'
    contenido.menu = ['menu-principal', 'menu2-alarma']

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form_a = AlarmaForm(request.POST)
        # check whether it's valid:
        if form_a.is_valid():
            post = form_a
            post.save()
            messages.success(request, 'Alarma registrada!')

            return HttpResponseRedirect('/alarmas')
        else:

            messages.error(request, 'Alerta!! La alarma nodo {} ya esta registrada. CONFIGURACION Tipo Alarma: {}, Parametro Operacional: {}'.format(form_a.data['name_alarma'],form_a.data['tipo_alarma'], form_a.data['parametro']))

            #return render(request, 'vista/error.html', )
    else:
        form_a = AlarmaForm()

        if request.method == 'GET':
            form_a = AlarmaForm()
            return render(request, 'vista/addAlarma.html', {'form_alarma': form_a, })

    return render(request, 'vista/addAlarma.html', {'cont': contenido,
                                                    'form_alarma': form_a})


def alarma(request):
    contenido = ContenidoContainer()
    contenido.user = request.user
    contenido.titulo = u'Alarma DMH'
    contenido.subtitulo = u'Mostrar Alarma'
    contenido.menu = ['menu-principal', 'menu2-alarma']

    datos = Alarma.objects.all()

    return render(request, 'vista/alarmas.html',
                  {'cont': contenido,
                   'data': datos
                   })


def show_alarma(request, id):
    contenido = ContenidoContainer()
    contenido.user = request.user
    contenido.titulo = u'Alarmas DMH'
    contenido.subtitulo = u'Mostrar detalle Alarma'
    contenido.menu = ['menu-principal', 'menu2-alarma']

    conf = Alarma.objects.get(id_alarma = id)
    form = AlarmaForm(instance=conf)

    return render(request, 'vista/alarma_detalle.html',
                  {'cont': contenido,
                   'form': form,
                   'id': conf.id_alarma
                   })

def del_alarma(request,id):

    if request.method == 'POST':
        conf = Alarma.objects.get(id_alarma=id)

        alarma_status = Alarma.objects.get(id_alarma=conf.id_alarma)
        alarma_status.hasConfig = False
        alarma_status.save()
        conf.delete()
    return HttpResponseRedirect('/alarmas')
    #return HttpResponseRedirect(reverse('vista/alarmas.html'))


def edit_alarma(request,id):
    contenido = ContenidoContainer()
    contenido.user = request.user
    contenido.titulo = u'Alarmas DMH'
    contenido.subtitulo = u'Editar configuración'
    contenido.menu = ['menu-principal', 'menu2-alarma']

    conf = Alarma.objects.get(id_alarma=id)

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AlarmaForm(request.POST,instance=conf)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('vista:alarma'))
             # if a GET (or any other method) we'll create a blank form
    else:
        form = AlarmaForm(instance=conf)
    return render(request, 'vista/addAlarma.html',
                  {'cont': contenido,
                   'form_alarma': form,
                   'id_alarma': conf.id_alarma,
                   'id_node': conf.name_alarma_id
                  })


# ***************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************

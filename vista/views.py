from django.shortcuts import render
from vista.functions import *
from models import NodeStatus, NodeConfig
import logging
logger = logging.getLogger('oritec')

def index(request):
    contenido=ContenidoContainer()
    contenido.user=request.user
    contenido.titulo=u'Flujometros DMH'
    contenido.subtitulo=u'Status del sistema'
    contenido.menu = ['menu-principal', 'menu2-resumen']

    nodos = NodeStatus.objects.all()

    return render(request, 'vista/index.html',
        {'cont': contenido,
         'nodos': nodos
        })
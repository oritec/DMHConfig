# -*- coding: utf-8 -*-
from django.forms import ModelForm
from models import NodeConfig, Eventos, Alarma


class NodeConfigForm(ModelForm):
    class Meta:
        model = NodeConfig
        fields = ['nodeId', 'flowSource', 'conversionFactor', 'executionPeriod','litresPerPulse','filterFrequency']
        labels = {
            "nodeId": "Nodo ID",
            "flowSource": "Señalización del flujo",
            "executionPeriod": "Periodo de envío de datos",
            "conversionFactor": "Factor de conversión",
            "litresPerPulse": "Litros por pulso",
            "filterFrequency": "Frecuencia de corte filtro 4-20 [mA]"
        }
    def __init__(self, *args, **kwargs):
        super(NodeConfigForm, self).__init__(*args, **kwargs)
        self.fields['nodeId'].widget.attrs['class'] = 'form-control'
        self.fields['flowSource'].widget.attrs['class'] = 'form-control'
        self.fields['conversionFactor'].widget.attrs['class'] = 'form-control'
        self.fields['executionPeriod'].widget.attrs['class'] = 'form-control'
        self.fields['litresPerPulse'].widget.attrs['class'] = 'form-control'
        self.fields['filterFrequency'].widget.attrs['class'] = 'form-control'

class EventoForm(ModelForm):
    class Meta:
        model = Eventos
        fields = ['id', 'inicio', 'fin', 'cerrado','maquina','tipoevento']
        labels = {
            "id": "ID Evento",
            "inicio": "Fecha Inicio Evento",
            "fin": "Fecha Termino Evento",
            "cerrado": "Estado",
            "maquina": "Inst. Emisor",
            "tipoevento" : "Evento"
        }

# ************************************************************************************

class AlarmaForm(ModelForm):
    class Meta:
        model = Alarma
        fields = ['id_alarma', 'name_alarma', 'tipo_alarma', 'parametro', ]
        labels = {
            "id_alarma": "ID Alarma",
            "name_alarma": "Nombre Nodo",
            "tipo_alarma": "Tipo Alarma",
            "parametro": "Parametro Operacion",
        }

    def __init__(self, *args, **kwargs):
        super(AlarmaForm, self).__init__(*args, **kwargs)
        #self.fields['id_alarma'].widget.attrs['class'] = 'form-control'

        self.fields['name_alarma'].widget.attrs['class'] = 'form-control'
        #self.fields['name_alarma'].queryset = NodeConfigForm.objects.filter()

        self.fields['tipo_alarma'].widget.attrs['class'] = 'form-control'
        self.fields['parametro'].widget.attrs['class'] = 'form-control'

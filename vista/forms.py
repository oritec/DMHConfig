# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from models import NodeConfig, Eventos, Alarma, SystemConfig
from django.core.validators import validate_ipv46_address

class NodeConfigForm(ModelForm):
    class Meta:
        model = NodeConfig
        fields = ['nodeId', 'flowSource', 'conversionFactor', 'executionPeriod','litresPerPulse','filterFrequency', 'offsetValue']
        labels = {
            "nodeId": "Nodo ID",
            "flowSource": "Señalización del flujo",
            "executionPeriod": "Periodo de envío de datos",
            "conversionFactor": "Factor de conversión",
            "litresPerPulse": "Litros por pulso",
            "filterFrequency": "Frecuencia de corte filtro 4-20 [mA]",
            "offsetValue": "Valor de calibración para sensor de nivel"
        }
    def __init__(self, *args, **kwargs):
        super(NodeConfigForm, self).__init__(*args, **kwargs)
        self.fields['nodeId'].widget.attrs['class'] = 'form-control'
        self.fields['flowSource'].widget.attrs['class'] = 'form-control'
        self.fields['conversionFactor'].widget.attrs['class'] = 'form-control'
        self.fields['executionPeriod'].widget.attrs['class'] = 'form-control'
        self.fields['litresPerPulse'].widget.attrs['class'] = 'form-control'
        self.fields['filterFrequency'].widget.attrs['class'] = 'form-control'
        self.fields['offsetValue'].widget.attrs['class'] = 'form-control'

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

class SystemConfigForm(ModelForm):
    class Meta:
        model = SystemConfig
        fields = ['http_dest', 'enable_send','id']
        labels = {
            "id": "ID Evento",
            "http_dest": "IP Base de datos",
            "enable_send": "Habilitar envio"
        }
    def __init__(self, *args, **kwargs):
        super(SystemConfigForm, self).__init__(*args, **kwargs)
        #self.fields['id_alarma'].widget.attrs['class'] = 'form-control'
        #self.fields['id'].widget = forms.HiddenInput()
        #self.fields['id'].widget = forms.HiddenInput()
        self.fields['http_dest'].widget.attrs['class'] = 'form-control'
        self.fields['enable_send'].widget.attrs['class'] = 'form-control'

    def clean_http_dest(self):
        data = self.cleaned_data['http_dest']
        validate_ipv46_address(data)
        return data

    def clean_enable_send(self):
        data = self.cleaned_data['enable_send']
        if (data != 1 and data != 0):
            raise forms.ValidationError("Valor sólo puede ser 1 o 0.")
        return data
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

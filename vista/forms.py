# -*- coding: utf-8 -*-
from django.forms import ModelForm
from models import NodeConfig

class NodeConfigForm(ModelForm):
    class Meta:
        model = NodeConfig
        fields = ['nodeId', 'flowSource', 'conversionFactor', 'executionPeriod','litresPerPulse']
        labels = {
            "nodeId": "Nodo ID",
            "flowSource": "Señalización del flujo",
            "executionPeriod": "Periodo de envío de datos",
            "conversionFactor": "Factor de conversión",
            "litresPerPulse": "Litros por pulso",
        }
    def __init__(self, *args, **kwargs):
        super(NodeConfigForm, self).__init__(*args, **kwargs)
        self.fields['nodeId'].widget.attrs['class'] = 'form-control'
        self.fields['flowSource'].widget.attrs['class'] = 'form-control'
        self.fields['conversionFactor'].widget.attrs['class'] = 'form-control'
        self.fields['executionPeriod'].widget.attrs['class'] = 'form-control'
        self.fields['litresPerPulse'].widget.attrs['class'] = 'form-control'
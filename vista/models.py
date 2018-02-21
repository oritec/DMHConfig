from __future__ import unicode_literals

from django.db import models

class FlowSources(models.Model):
    name = models.TextField(null=False)
    code = models.IntegerField(blank=False, null=False)
    class Meta:
        db_table = 'flow_sources'
    def __str__(self):
        return self.name

class Data(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    nodeId = models.IntegerField(null=False, blank=False)
    msgTime = models.DateTimeField(auto_now_add=True)
    sent = models.BooleanField(default=False)
    flujo = models.FloatField(null=False, blank=False)
    totalizador = models.FloatField(null=False, blank=False)
    corriente = models.FloatField(null=False, blank=False, default=0)
    class Meta:
        db_table = 'data'


class NodeConfig(models.Model):
    nodeId = models.IntegerField(primary_key=True, null=False)
    flowSource = models.ForeignKey('flowSources', on_delete=models.CASCADE)
    conversionFactor = models.FloatField(null=True,blank=True, default=15.0)
    executionPeriod = models.IntegerField(blank=False, null=False, default=10)
    litresPerPulse = models.IntegerField(blank=True, null=True, default=500)
    filterFrequency = models.FloatField(null=True,blank=True, default=1.0)
    class Meta:
        db_table = 'node_config'
        #unique_together = (('turbina', 'inicio'),)
    def __str__(self):
            return 'Nodo ' + str(self.nodeId)

class NodeStatus(models.Model):
    nodeId = models.AutoField(primary_key=True, null=False)
    batteryLevel = models.FloatField(null=False,blank=False)
    lastRSSI = models.IntegerField(null=False, blank=False, default=0)
    lastSNR = models.IntegerField(null=False, blank=False,default=0)
    msgTime = models.DateTimeField(auto_now_add=True)
    hasConfig = models.BooleanField(default=False)
    sent = models.BooleanField(default=False)
    class Meta:
        db_table = 'node_status'

class Analisis(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    nodeId = models.IntegerField(null=False, blank=False)
    temperatura = models.FloatField(null=False, blank = False)
    potencia = models.FloatField(null=False, blank = False)
    voltage = models.FloatField(null=False, blank = False)
    corriente = models.FloatField(null=False, blank = False)
    carga = models.IntegerField(null=False, blank=False)
    fault = models.IntegerField(null=False, blank=False)
    msgTime = models.DateTimeField(auto_now_add=True)
    sent = models.BooleanField(default=False)

    class Meta:
        db_table = 'analisis'

class Eventos(models.Model):
    TITLE_CHOICES = (
        ('1', 'CERRADO'),
        ('0', 'ABIERTO'),
    )
    id = models.AutoField(primary_key=True, null=False)
    inicio = models.DateTimeField(null=True)
    fin = models.DateTimeField(null=True)
    cerrado = models.IntegerField(null=False, blank=False)
    maquina = models.CharField(max_length=20)
    tipoevento = models.CharField(max_length=20)

    class Meta:
        db_table = 'tablaeventos'

# **************************************************************************

class Alarma(models.Model):
    TITLE_CHOICES = (
        ('ALTO', 'alto'),
        ('BAJO', 'bajo'),
    )

    id_alarma = models.AutoField(primary_key=True, null=False)
    #id_alarma = models.IntegerField(primary_key=True, null=False)
    name_alarma = models.ForeignKey(NodeConfig, on_delete=models.CASCADE )
    #name_alarma = models.CharField(max_length=30)
    tipo_alarma = models.CharField(max_length=5, choices=TITLE_CHOICES)
    parametro = models.FloatField(null=True,blank=True, default=0.0)

    class Meta:
        db_table = 'tabla_alarma'
        unique_together = (('name_alarma', 'tipo_alarma'),)



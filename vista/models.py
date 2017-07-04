from __future__ import unicode_literals

from django.db import models

class flowSources(models.Model):
    name = models.TextField(null=False)
    code = models.IntegerField(blank=False, null=False)
    class Meta:
        db_table = 'flow_sources'

class NodeConfig(models.Model):
    nodeId = models.AutoField(primary_key=True, null=False)  # AutoField?
    flowSource = models.ForeignKey('flowSources', on_delete=models.CASCADE)
    conversionFactor = models.FloatField(null=True,blank=True)
    executionPeriod = models.IntegerField(blank=False, null=False, default=10)
    litresPerPulse = models.IntegerField(blank=True, null=True)
    class Meta:
        db_table = 'node_config'
        #unique_together = (('turbina', 'inicio'),)

class NodeStatus(models.Model):
    nodeId = models.AutoField(primary_key=True, null=False)
    batteryLevel = models.FloatField(null=False,blank=False)
    msgTime = models.DateTimeField(auto_now_add=True)
    hasConfig = models.BooleanField(default=False)
    sent = models.BooleanField(default=False)
    class Meta:
        db_table = 'node_status'

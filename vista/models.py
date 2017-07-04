from __future__ import unicode_literals

from django.db import models

class FlowSources(models.Model):
    name = models.TextField(null=False)
    code = models.IntegerField(blank=False, null=False)
    class Meta:
        db_table = 'flow_sources'
    def __str__(self):
        return self.name

class NodeConfig(models.Model):
    nodeId = models.IntegerField(primary_key=True, null=False)
    flowSource = models.ForeignKey('flowSources', on_delete=models.CASCADE)
    conversionFactor = models.FloatField(null=True,blank=True, default=18.75)
    executionPeriod = models.IntegerField(blank=False, null=False, default=10)
    litresPerPulse = models.IntegerField(blank=True, null=True, default=500)
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

from django.db import models


class RoadAccidentPoint(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    type = models.CharField(max_length=100)
    geometry = models.JSONField(null=True)
    properties = models.JSONField(null=True)
    inwater = models.BooleanField()
    coordinatesisaccurate = models.BooleanField()
    inregion = models.JSONField(null=True)
    onroad = models.BooleanField()
    distancedif = models.CharField(max_length=100)
    yandexgeocoder = models.JSONField(null=True)
    adminlevel = models.JSONField(null=True)
    dtptime = models.DateTimeField()
    valid = models.BooleanField()
    validpercent = models.IntegerField()

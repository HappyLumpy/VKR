from django.db import models


class RoadAccidentPoint(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    type = models.CharField(max_length=100)
    geometry = models.JSONField(null=True)
    properties = models.JSONField(null=True)
    inwater = models.BooleanField()
    coordinatesIsAccurate = models.BooleanField()
    inRegion = models.JSONField(null=True)
    onRoad = models.BooleanField()
    distanceDif = models.FloatField(null=True, default=None)
    yandexGeocoder = models.JSONField(null=True, default=None)
    adminLevel = models.JSONField(null=True)
    dtpTime = models.JSONField(null=True)
    valid = models.BooleanField()
    validPercent = models.IntegerField()


class ConcentrationAccident(models.Model):
    listid = models.JSONField()
    coordinates = models.JSONField()

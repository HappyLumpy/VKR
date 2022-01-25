from .models import RoadAccidentPoint
from rest_framework import serializers
from rest_framework.views import APIView
from django.contrib.auth.models import User
from datetime import datetime
from rest_framework.serializers import ModelSerializer, Serializer, ListField, ChoiceField, BooleanField


class PointSerializer(serializers.ModelSerializer):

    def to_internal_value(self, data):
        data['inwater'] = data.pop('inWater')
        data['id'] = data['_id']['$oid']
        data.pop('_id')
        return data

    class Meta:
        model = RoadAccidentPoint
        fields = ('id', 'type', 'inwater')


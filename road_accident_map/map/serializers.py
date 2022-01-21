from rest_framework import serializers
from .models import RoadAccidentPoint
from django.contrib.auth.models import User
from datetime import datetime
from rest_framework.serializers import ModelSerializer, Serializer, ListField, ChoiceField, BooleanField


class PointSerializer(serializers.ModelSerializer):
    inwater = serializers.BooleanField(source='inWater')

    class Meta:
        model = RoadAccidentPoint
        fields = "__all__"

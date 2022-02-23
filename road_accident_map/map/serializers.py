from .models import RoadAccidentPoint, ConcentrationAccident
from rest_framework import serializers


class PointSerializer(serializers.ModelSerializer):

    def to_internal_value(self, data):
        data['inwater'] = data.pop('inWater')
        data['id'] = data['_id']['$oid']
        data.pop('_id')
        return data

    class Meta:
        model = RoadAccidentPoint
        fields = '__all__'


class PointUpploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadAccidentPoint
        fields = ('type', 'geometry', 'properties')


class PointLoad(serializers.ModelSerializer):
    class Meta:
        model = RoadAccidentPoint
        fields = ('geometry',)


class ConcentrationPolygonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConcentrationAccident
        fields = ('coordinates',)


class ConcentrationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConcentrationAccident
        fields = ('coordinates', 'listid')

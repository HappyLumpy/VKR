from collections import OrderedDict

from django.db.models import Q
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import RoadAccidentPoint
from .serializers import *
from django.shortcuts import render
from django.conf import settings


def mappoint(request):
    return render(request, 'map/mappoint.html')


def mappoly(request):
    return render(request, 'map/mappoly.html')


class PointView(APIView):
    def get(self, request):
        point = RoadAccidentPoint.objects.all()
        serializer = PointUpploadSerializer(point, many=True)
        return Response(serializer.data)


class ConcentrationView(APIView):
    def get(self, request):
        polygons = ConcentrationAccident.objects.all()
        serializerpolygons = ConcentrationPolygonSerializer(polygons, many=True)
        return Response(serializerpolygons.data)

class ConcentrationPointView(APIView):
    def get(self, request):
        polygons = ConcentrationAccident.objects.all()
        serializerpolygons = ConcentrationPointSerializer(polygons, many=True)
        for data in serializerpolygons.data:
            for _id in data['listid']:
                point = RoadAccidentPoint.objects.filter(pk=_id)
                new_point = PointUpploadSerializer(point, many=True)

            return Response(new_point.data)

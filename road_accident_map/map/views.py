from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from django.shortcuts import render



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




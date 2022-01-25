from django.contrib import admin
from .models import *

@admin.register(RoadAccidentPoint)
class MapAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'geometry')
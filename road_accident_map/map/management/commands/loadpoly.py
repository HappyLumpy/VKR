from django.core.management import BaseCommand
import json
from map.serializers import *
from math import sin, cos, sqrt, atan2, radians


class Command(BaseCommand):
    help = 'add polygons in DB from Json'

    def add_arguments(self, parser):
        parser.add_argument('Json_File')

    def handle(self, *args, **options):
        coorddict = {}
        fulldict = {}
        key = 1
        R = 6371

        with open(options['Json_File'], encoding='utf-8-sig') as json_file:
            json_data = json.loads(json_file.read())
            for new_data in json_data:
                fulldict[new_data['_id']['$oid']] = new_data["geometry"]["coordinates"]
            for new_data in json_data:
                dictIdCoord = {}
                dictIdCoord['listid'] = [new_data['_id']['$oid']]
                dictIdCoord['coordinates'] = [new_data["geometry"]["coordinates"]]
                coorddict[key] = dictIdCoord
                for ID, coords in fulldict.items():
                    lat1 = radians(new_data["geometry"]["coordinates"][1])
                    lon1 = radians(new_data["geometry"]["coordinates"][0])
                    lat2 = radians(coords[1])
                    lon2 = radians(coords[0])
                    dlon = lon2 - lon1
                    dlat = lat2 - lat1
                    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
                    c = 2 * atan2(sqrt(a), sqrt(1 - a))
                    distance = R * c * 1000
                    if 0 < distance <= 200:
                        coorddict[key]['listid'].append(ID)
                        coorddict[key]['coordinates'].append(coords)
                key += 1
            for keys in coorddict:
                if len(coorddict[keys]['coordinates']) >= 3:
                    new_list = ConcentrationListSerializer(data=coorddict[keys])
                    if new_list.is_valid():
                        new_list.save()

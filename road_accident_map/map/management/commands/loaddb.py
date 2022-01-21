from django.core.management import BaseCommand
import json
from map.serializers import *
from map.models import RoadAccidentPoint


class Command(BaseCommand):
    help = 'Add DB from Json'

    def add_arguments(self, parser):
        parser.add_argument('Json_File')

    def handle(self, *args, **options):
        with open(options['Json_File'], encoding='utf-8-sig') as json_file:
            json_data = json.loads(json_file.read())
            counter = 0
            for data in json_data:

                # if data.get('distanceDif') is None:
                #     data['distanceDif'].required = None
                # if data.get('yandexGeocoder') is None:
                #     data['yandexGeocoder'] = None
                # new_data = {'id': data['_id']['$oid'], 'type': data['type'], 'geometry': data['geometry'],
                #                 'properties': data['properties'], 'inwater': data['inWater'],
                #                 'coordinatesisaccurate': data['coordinatesIsAccurate'], 'inregion': data['inRegion'],
                #                 'onroad': data['onRoad'], 'distancedif': data['distanceDif'],
                #                 'yandexgeocoder': data['yandexGeocoder'], 'adminlevel': data['adminLevel'],
                #                 'dtptime': data['dtpTime'], 'valid': data['valid'],
                #                 'validpercent': data['validPercent']}
                new_point = PointSerializer(data=data)

                if new_point.is_valid():
                    counter +=1
                    new_point.save()
                    print(counter)




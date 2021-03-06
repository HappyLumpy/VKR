from django.core.management import BaseCommand
import json
from map.serializers import *


class Command(BaseCommand):
    help = 'Add point in DB from Json'

    def add_arguments(self, parser):
        parser.add_argument('Json_File')

    def handle(self, *args, **options):
        with open(options['Json_File'], encoding='utf-8-sig') as json_file:
            json_data = json.loads(json_file.read())
            for new_data in json_data:
                new_point = PointSerializer(data=new_data)
                if new_point.is_valid():
                    new_point.save()



from django.core.management import BaseCommand
import json
from map.models import RoadAccidentPoint


class Command(BaseCommand):
    help = 'Add DB from Json'

    def add_arguments(self, parser):
        parser.add_argument('Json_File')

    def handle(self, *args, **options):
        with open(options['Json_File'], encoding='utf-8-sig') as json_file:
            json_data = json.loads(json_file.read())
            for data in json_data:
                for i in data:
                    if i == '_id':
                        RoadAccidentPoint.id.save(data[i])
                    if i == 'type':
                        RoadAccidentPoint.type.save(data[i])
                    if i == 'geometry':
                        RoadAccidentPoint.geometry.save(data[i])

            # self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"'))

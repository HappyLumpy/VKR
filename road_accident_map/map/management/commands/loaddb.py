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
                if data.keys() == '_id':
                    RoadAccidentPoint.id.save(data)
                if data.keys() == 'type':
                    RoadAccidentPoint.id.save(data)
                if data.keys() == 'geometry':
                    RoadAccidentPoint.id.save(data)

            self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"'))

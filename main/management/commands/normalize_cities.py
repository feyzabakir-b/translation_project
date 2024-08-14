from django.core.management.base import BaseCommand
from main.models import City

class Command(BaseCommand):
    help = 'Normalizes existing city names'

    def handle(self, *args, **options):
        cities = City.objects.all()
        for city in cities:
            city.save()  # This will trigger the save method and update normalized_name
        self.stdout.write(self.style.SUCCESS('Successfully normalized all city names'))
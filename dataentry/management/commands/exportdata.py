import csv
import datetime
from django.core.management.base import BaseCommand, CommandError
from django.apps import apps

class Command(BaseCommand):
    help = 'Export data from any model to a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('model_name', type=str, help='Name of the model to export (e.g., Student)')

    def handle(self, *args, **options):
        model_name = options['model_name']
        model = None

        # Search through installed apps for the model
        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label, model_name)
                if model:
                    break
            except LookupError:
                continue

        if not model:
            raise CommandError(f'Model "{model_name}" not found in any app.')

        # Get all objects
        objects = model.objects.all()

        if not objects.exists():
            self.stdout.write(self.style.WARNING('No data to export.'))
            return

        # Get model fields dynamically
        field_names = [field.name for field in model._meta.fields]

        # Create timestamped filename
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        file_path = f'exported_{model_name.lower()}_data_{timestamp}.csv'

        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(field_names)  # Header row

            for obj in objects:
                writer.writerow([getattr(obj, field) for field in field_names])

        self.stdout.write(self.style.SUCCESS(f'Data exported successfully to {file_path}'))

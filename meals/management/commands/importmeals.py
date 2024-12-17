# mealplanner/meals/management/commands/importmeals.py

import csv
import os
from django.core.management.base import BaseCommand
from meals.models import Meal

class Command(BaseCommand):
    help = 'Import meals from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f'File {file_path} does not exist.'))
            return

        with open(file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    meal = Meal(
                        name=row['name'],
                        description=row['description'],
                        image=row['image']
                    )
                    meal.save()
                    self.stdout.write(self.style.SUCCESS(f'Successfully added meal: {row["name"]}'))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Error adding meal: {row["name"]}, Error: {e}'))

import django
import pandas as pd

import sys
import os

# Add the project directory to the Python path
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_path)

# Set the default settings module for Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mealplanner.settings')

import django
django.setup()

from meals.models import Meal

# Load the Excel file
data_path = r'C:\Users\ngufor\Desktop\Aisha\nchang\Projects\MealPlanner\mealplanner\meals\data\CMR.xlsx'
data = pd.read_excel(data_path)

# Import data into the database
for index, row in data.iterrows():
    try:
        meal = Meal(
            name=row['Name'],
            description=row['Description'],
            main_ingredient=row['Main Ingredient'],
            recipe_link=row['Recipe Link'],
            image=row['Image URL'],
            weight=float(row['Weight']),  # Ensure conversion to float
            ease=float(row['Ease'])        # Ensure conversion to float
        )
        meal.save()
    except ValueError as e:
        print(f"Error processing row {index}: {e}")

print("Data imported successfully!")

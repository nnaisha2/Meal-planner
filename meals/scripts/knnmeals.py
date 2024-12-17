from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
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

# Load data
file_path = r'C:\Users\ngufor\Desktop\Aisha\nchang\Projects\MealPlanner\mealplanner\meals\data\CMR.xlsx'
data = pd.read_excel(file_path)

# Prepare features and labels
X = data[['Weight', 'Ease']]  # Features
y = data['Name']  # Target (meal names)

# Initialize the KNN model with 5 neighbors
knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X, y)

def recommend_meals(user_weight, user_ease, k=5):
    """
    Recommend meals based on user preferences using K-Nearest Neighbors.
    :param user_weight: User's desired weight.
    :param user_ease: User's desired ease.
    :param k: Number of neighbors to consider.
    :return: List of recommended meal names.
    """
    user_preferences = [[user_weight, user_ease]]
    distances, indices = knn_model.kneighbors(user_preferences, n_neighbors=k)

    recommendations = []
    for idx in indices.flatten():
        recommendations.append(data.iloc[idx]['Name'])

    return recommendations

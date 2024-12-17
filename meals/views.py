from django.shortcuts import render
from .models import Meal
from .scripts.knnmeals import recommend_meals  # Import the KNN recommendation function

def recommend_meals_view(request):
    if request.method == 'POST':
        user_weight = float(request.POST.get('weight'))
        user_ease = float(request.POST.get('ease'))

        # Get meal recommendations
        recommendations = recommend_meals(user_weight, user_ease)

        # Fetch details for each recommended meal
        recommended_meals = []
        for meal_name in recommendations:
            try:
                meal = Meal.objects.get(name=meal_name)
                recommended_meals.append({
                    'name': meal.name,
                    'description': meal.description,
                    'image_url': meal.image.url if meal.image else None,  # Use .url for local images
                    'recipe_link': meal.recipe_link,
                    'main_ingredients': meal.main_ingredient,
                })
            except Meal.DoesNotExist:
                # Skip meals not found in the database
                continue

        return render(request, 'meals/recommendations.html', {'recommended_meals': recommended_meals})

    return render(request, 'meals/recommend_form.html')

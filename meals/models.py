from django.db import models

class Meal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='meals/')  # Store images in /media/meals/
    recipe_link = models.URLField()
    main_ingredient = models.CharField(max_length=1000)
    weight = models.FloatField(default=0.0)
    ease = models.FloatField(default=0.0)

    def __str__(self):
        return self.name



class MealPlan(models.Model):
    date = models.DateField()
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)

    def __str__(self):
        return f"Meal Plan for {self.date}"


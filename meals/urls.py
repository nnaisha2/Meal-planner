from django.urls import path
from . import views

urlpatterns = [
    path('', views.recommend_meals_view, name='recommend_meals'),
]
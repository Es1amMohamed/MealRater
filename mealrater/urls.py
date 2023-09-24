from django.urls import path
from .views import *

app_name = 'mealrater'

urlpatterns = [
    path('',MealListApi.as_view(),name='meal_list'),
    path('rate',RatingPkApi.as_view(),name='rating_api')
]

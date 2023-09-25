from django.urls import path
from .views import *
from django.conf.urls import include
from rest_framework import routers


router = routers.DefaultRouter()
router.register('meals',MealListApi)
router.register('rating',RatingPkApi)

app_name = 'mealrater'

urlpatterns = [
    path('',include(router.urls)),
]

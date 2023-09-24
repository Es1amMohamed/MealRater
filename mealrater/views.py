from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import MealSerializer , RatingSerializer

# Create your views here.

class MealListApi(generics.ListCreateAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    

class RatingPkApi(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
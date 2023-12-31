from rest_framework import serializers
from .models import *


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ["id", "title", "description", "num_of_ratings", "avg_rating"]


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ["id", "stars", "user", "meal"]


class USerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "id"]

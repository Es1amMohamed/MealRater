from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import *
from .serializers import MealSerializer, RatingSerializer, USerSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = USerSerializer
    authentication_classes = [
        TokenAuthentication,
    ]
    permission_classes = [
        IsAuthenticated,
    ]


class MealListApi(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    authentication_classes = [
        TokenAuthentication,
    ]
    permission_classes = [
        IsAuthenticated,
    ]

    @action(detail=True, methods=["post"])
    def rate_meal(self, request, pk=None):
        if "stars" in request.data:
            if 1 <= int(request.data["stars"]) <= 5:
                # username = request.data['username']
                # user = User.objects.get(username=username)
                user = request.user
                meal = Meal.objects.get(id=pk)
                stars = request.data["stars"]

                try:
                    rate = Rating.objects.get(user=user.id, meal=meal.id)
                    rate.stars = stars
                    rate.save()
                    serializer = RatingSerializer(rate, many=False)
                    json = {"message": "Meal Rate Update", "result": serializer.data}

                    return Response(json, status=status.HTTP_200_OK)
                except:
                    rate = Rating.objects.create(user=user, stars=stars, meal=meal)
                    serializer = RatingSerializer(rate, many=False)
                    json = {"message": "Meal Rate Created", "result": serializer.data}
                    return Response(json, status=status.HTTP_200_OK)
            else:
                json = {"message": "stars Minimum 1 and Maximum 5 "}
            return Response(json, status=status.HTTP_400_BAD_REQUEST)
        else:
            json = {"message": "stars not provided"}
            return Response(json, status=status.HTTP_400_BAD_REQUEST)


class RatingPkApi(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = [
        TokenAuthentication,
    ]
    permission_classes = [
        IsAuthenticated,
    ]

    def create(self, request, *args, **kwargs):
        response = {"message": "Invalid way to create rate"}

        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        response = {"message": "Invalid way to update rate"}

        return Response(response, status=status.HTTP_400_BAD_REQUEST)

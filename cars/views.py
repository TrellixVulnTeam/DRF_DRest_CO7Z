from django.shortcuts import render
from rest_framework import generics
from cars.serializers import CarDetailSerializer, CarListSerializer
from cars.models import Car
from cars.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
# Create your views here.

class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer #создание записи


class CarListView(generics.ListAPIView): 
    serializer_class= CarListSerializer
    queryset= Car.objects.all()
    permission_classes=(IsAdminUser, )#(IsAuthenticated, ) # просмотр записей только авторизированным пользователям


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):    
    serializer_class= CarDetailSerializer
    queryset= Car.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes=(IsOwnerOrReadOnly, ) #редактирование записи может произвести только создатель этой записи



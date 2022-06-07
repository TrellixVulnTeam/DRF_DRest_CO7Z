from django.contrib import admin
from django.urls import path
from cars.views import *

app_name ='car'
urlpatterns = [
    path('car/create/', CarCreateView.as_view()), #окно для добавления новых и редактирования старых записей 
    path('all/', CarListView.as_view()), # предоставление всех записей
    path('car/detail/<int:pk>/', CarDetailView.as_view()), #педоставление записи по primary key

]

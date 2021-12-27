from django.contrib import admin
from django.urls import path, include
from person.views import *

urlpatterns = [
    path('person/add/', PersonCreateView.as_view()),
    path('all/', PersonListView.as_view()),
    path('person/detail/<int:pk>', PersonDetailView.as_view())
]
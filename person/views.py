from django.shortcuts import render
from rest_framework import generics
from person.sterializers import *
from person.models import Person

class PersonCreateView(generics.CreateAPIView):
    serializer_class = PersonDetailSerializer

class PersonListView(generics.ListAPIView):
    serializer_class = PersonListSerializer
    queryset = Person.objects.all()

class PersonDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PersonDetailSerializer
    queryset = Person.objects.all()
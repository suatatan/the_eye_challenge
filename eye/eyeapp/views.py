from django.shortcuts import render
from rest_framework import viewsets
from eyeapp.models import Event,Application
from eyeapp.serializers import ApplicationSerializer,EventSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class KitapViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

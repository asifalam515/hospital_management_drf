from django.shortcuts import render
from rest_framework import viewsets
from service.models import Service
from service.serializers import ServiceSerializers
# Create your views here.
class ServiceViewSet(viewsets.ModelViewSet):
    queryset =Service.objects.all()
    serializer_class = ServiceSerializers
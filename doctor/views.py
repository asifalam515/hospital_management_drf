from django.shortcuts import render
from doctor.models import Doctor,AvailableTime,Specialization,Designation,Review
from doctor.serializers import DoctorSerializers,AvailableTimeSerializers,SpecializationSerializers,DesignationSerializers,Review


# Create your views here.
from rest_framework import viewsets


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializers
    
    def get_queryset(self):
        queryset= super().get_queryset()
        doctor_id = self.request.query_params.get('doctor_id')
        if doctor_id:
            queryset = queryset.filter(doctor = doctor_id)
        return queryset
    
    
class AvailableTimeViewSet(viewsets.ModelViewSet):
    queryset = AvailableTime.objects.all()
    serializer_class = AvailableTimeSerializers
    
    
class SpecializationViewSet(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializers
    
class DesignationViewSet(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializers
    
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = DesignationSerializers
    

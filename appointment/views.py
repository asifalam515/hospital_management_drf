from django.shortcuts import render
from appointment.models import Appointment
from appointment.serializers import AppointmentSerializers
from rest_framework import viewsets
# Create your views here.

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializers

    #custom query kora
    # def get_queryset(self):
    #     queryset = super().get_queryset() #normally  8 no line ke niye aslam ba parent inherit krolam
    #     patient_id = self.request.query_params.get('patient_id')
    #     if patient_id:
    #         queryset = queryset.filter(patient_id = patient_id)
            
    #     return queryset
      
    def get_queryset(self):
        queryset=  super().get_queryset()
        patient_id =self.request.query_params.get('patient_id')
        if patient_id:
            queryset = queryset.filter(patient_id = patient_id)
        return queryset
                  
        
        
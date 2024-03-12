from django.shortcuts import render
from patient.models import Patient
from patient.serializers  import PatientSerializers,RegistrationSerializers
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializers

class UserRegistrationApiView(APIView):
    serializer_class = RegistrationSerializers
    
    def post(self,request):
        serializer = self.serializer_class(data =request.data)
       
        if serializer.is_valid():
            user = serializer.save()
            return Response(" form done")
        
        return Response(serializer.errors)
    
    
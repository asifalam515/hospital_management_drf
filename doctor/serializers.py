from rest_framework import serializers
from doctor.models import Doctor,AvailableTime,Designation,Specialization,Review

class DoctorSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    available_time = serializers.StringRelatedField(many =True)
    designation=serializers.StringRelatedField(many =True)
    specialization=serializers.StringRelatedField(many =True)

    class Meta:
        model = Doctor
        fields ='__all__'
        
class SpecializationSerializers(serializers.ModelSerializer):

    class Meta:
        model = Specialization
        fields ='__all__'
        
        
class AvailableTimeSerializers(serializers.ModelSerializer):

    class Meta:
        model = AvailableTime
        fields ='__all__'
        
        
class DesignationSerializers(serializers.ModelSerializer):

    class Meta:
        model = Designation
        fields ='__all__'

class ReviewSerializers(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields ='__all__'
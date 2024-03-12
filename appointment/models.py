from django.db import models
from patient.models import Patient
from doctor.models import Doctor,AvailableTime
# Create your models here.
APPOINTMENT_TYPE=[
    ("Online","Online"),
    ("Offline","Offline"),
    
]
APPOINTMENT_STATUS=[
    ("Pending","Pending"),
    ("Running","Running"),
    ("Completed","Completed"),
]

class Appointment(models.Model):
    patient = models.ForeignKey(Patient,on_delete = models.CASCADE)
    doctor = models.ForeignKey(Doctor,on_delete = models.CASCADE)
    appointment_status = models.CharField(choices =APPOINTMENT_STATUS,default = "Pending",max_length=10)
    appointment_type = models.CharField(choices =APPOINTMENT_TYPE,max_length=10)
    symptoms = models.CharField(max_length=10)
    time = models.ForeignKey(AvailableTime,on_delete= models.CASCADE) 
    cancel = models.BooleanField(default = False)
    
    def __str__(self) -> str:
        return f"Doctor : {self.doctor.user.first_name} ,Patient :{self.patient.user.first_name}"
    

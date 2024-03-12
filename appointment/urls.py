from django.urls import path,include
from rest_framework.routers import DefaultRouter
from appointment.models import Appointment
from appointment.views import AppointmentViewSet


router = DefaultRouter()
router.register("",AppointmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
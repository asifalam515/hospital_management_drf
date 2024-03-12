from django.urls import path, include
from rest_framework.routers import DefaultRouter
from patient.views import PatientViewSet,UserRegistrationApiView

# Create a router and register our ViewSets with it.
router = DefaultRouter()

router.register("list",PatientViewSet,basename='list'),

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationApiView.as_view(),name='register'),
]
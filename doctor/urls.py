from django.urls import path, include
from rest_framework.routers import DefaultRouter

from doctor.views import DoctorViewSet,SpecializationViewSet,AvailableTimeViewSet,ReviewViewSet,DesignationViewSet

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register('list',DoctorViewSet )
router.register('specialization',SpecializationViewSet )
router.register('available_time',AvailableTimeViewSet )
router.register('reviews',ReviewViewSet )
router.register('designation',DesignationViewSet )

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
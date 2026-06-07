from django.urls import path
from . import api_views

urlpatterns = [
    path('doctors/', api_views.api_doctors, name='api_doctors'),
    path('appointments/', api_views.api_appointments, name='api_appointments'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('getall/', views.getAll),  # FIXED
    path('getBy/<int:id>/', views.getById),  # FIXED
    path('patient/', views.addPatient),  # FIXED
    path('updatePatient/<int:id>/', views.updatePatient),  # FIXED
    path('deletePatient/<int:id>/', views.deletePatient),  # FIXED
]
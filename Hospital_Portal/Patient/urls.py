from django.urls import path
from . import views

urlpatterns = [
    path('getall/', views.getAll),
    path('getBy/<int:id>/', views.getById),
    path('patient/', views.addPatient),
    path('updatePatient/<int:id>/', views.updatePatient),
    path('deletePatient/<int:id>/', views.deletePatient),
]
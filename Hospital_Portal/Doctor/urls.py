from django.urls import path
from . import views

urlpatterns = [
    path('getAll/', views.getAll),
    path('getBy/<int:id>/', views.getById),
    path('addDoctor/', views.addDoctor),
    path('updateDoctor/<int:id>/', views.updateDoctor),
    path('deleteDoctor/<int:id>/', views.deleteDoctor),
]

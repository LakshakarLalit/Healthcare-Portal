from django.urls import path
from . import views

urlpatterns = [
    path('getAll/', views.getAll),
    path('getBy/<int:id>/', views.getById),
    path('book/', views.bookAppointment),
    path('update/<int:id>/', views.updateAppointment),
    path('delete/<int:id>/', views.deleteAppointment),
]

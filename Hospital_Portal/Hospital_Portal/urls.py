from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('doctor/', include('Doctor.urls')),
    path('patient/', include('Patient.urls')),
    path('appointment/', include('Appointment.urls')),
    path('admin/', admin.site.urls),
]
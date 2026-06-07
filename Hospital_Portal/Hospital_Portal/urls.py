from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('Doctor.urls')),
    path('patient/', include('Patient.urls')),
    path('appointment/', include('Appointment.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('Hospital_Portal.api_urls')),
]
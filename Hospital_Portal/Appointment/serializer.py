from rest_framework import serializers
from .models import Appointment
from Doctor.serializer import DoctorSerializer
from Patient.serializer import PatientSerializer

class AppointmentSerializer(serializers.ModelSerializer):
    doctor_detail = DoctorSerializer(source='doctor', read_only=True)
    patient_detail = PatientSerializer(source='patient', read_only=True)

    class Meta:
        model = Appointment
        fields = '__all__'

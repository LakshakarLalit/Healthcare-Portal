from rest_framework.serializers import ModelSerializer
from .models import Doctor

class DoctorSerializer(ModelSerializer):
    class meta:
        model = Doctor
        fields = '__all__'
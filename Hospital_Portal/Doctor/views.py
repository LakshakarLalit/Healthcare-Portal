from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Doctor
from .serializer import DoctorSerializer

# Create your views here.

@api_view(['GET'])
def getAll(request):
    allDoctor = Doctor.objects.all()
    data = DoctorSerializer(allDoctor, many=True).data
    return Response({'message': "Success", "data": data})

@api_view(['GET'])
def getById(request, id):
    try:
        doctor = Doctor.objects.get(id=id)
        data = DoctorSerializer(doctor).data
        return Response({"message": "Success", "data": data})
    
    except Doctor.DoesNotExist:
        return Response({"message": "Not Found", "data": {}})

@api_view(['POST'])
def addDoctor(request):
    newDoctor = request.data
    doctor = DoctorSerializer(data = newDoctor)
    if doctor.is_valid():
        doctor.save()
        return Response({"message": "Successfully Added", "data": doctor.data})
    return Response({"message": "Error", "data": doctor.errors})

@api_view(['PUT'])
def updateDoctor(request, id):
    try:
        doctor = Doctor.objects.get(id=id)
        serializer = DoctorSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Success", "data": serializer.data})
        return Response({"message": "Error", "data": serializer.errors})
    except Doctor.DoesNotExist:
        return Response({"message": "Error", "data": "Doctor not found"})

@api_view(['DELETE'])
def deleteDoctor(request, id):
    try:
        doctor = Doctor.objects.get(id=id)
        doctor.delete()
        return Response({"message": "Success", "data": {}})
    except Doctor.DoesNotExist:
        return Response({"message": "Error", "data": "Doctor not found"})
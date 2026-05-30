from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Patient
from .serializer import PatientSerializer


@api_view(['GET'])
def getAll(request):
    allPatient = Patient.objects.all()
    data = PatientSerializer(allPatient, many=True).data
    return Response({"message": "Success", "data": data})

@api_view(['GET'])
def getById(request, id):
    try:
        Patient = Patient.objects.get(id=id)
        data = PatientSerializer(Patient).data
        return Response({"message": "Success", "data": data})
    except Patient.DoesNotExist:
        return Response({"message": "Not Found", "data": {}})

@api_view(['POST'])
def addPatient(request):
    newPatient = request.data
    Patient = PatientSerializer(data=newPatient)
    if newPatient.is_valid():
        newPatient.save()
        return Response({"message": "Success", "data": newPatient.data})
    return Response({"message": "Error", "data": newPatient.errors})

@api_view(['PUT'])
def updatePatient(request, id):
    try:
        Patient = Patient.objects.get(id=id)
        serializer = PatientSerializer(Patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Success", "data": serializer.data})
        return Response({"message": "Error", "data": serializer.errors})
    except Patient.DoesNotExist:
        return Response({"message": "Error", "data": "Patient not found"})

@api_view(['DELETE'])
def deletePatient(request, id):
    try:
        Patient = Patient.objects.get(id=id)
        Patient.delete()
        return Response({"message": "Success", "data": {}})
    except Patient.DoesNotExist:
        return Response({"message": "Error", "data": "Patient not found"})
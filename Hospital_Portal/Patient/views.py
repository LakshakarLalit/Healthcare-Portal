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
        patient = Patient.objects.get(id=id)  
        data = PatientSerializer(patient).data  
        return Response({"message": "Success", "data": data})
    except Patient.DoesNotExist:
        return Response({"message": "Not Found", "data": {}})

@api_view(['POST'])
def addPatient(request):
    newPatient = request.data
    serializer = PatientSerializer(data=newPatient)  # FIXED
    if serializer.is_valid():  # FIXED: 'newPatient.is_valid()' → 'serializer.is_valid()'
        serializer.save()  # FIXED
        return Response({"message": "Success", "data": serializer.data})  # FIXED
    return Response({"message": "Error", "data": serializer.errors})  # FIXED

@api_view(['PUT'])
def updatePatient(request, id):
    try:
        patient = Patient.objects.get(id=id)  # FIXED: 'Patient' → 'patient'
        serializer = PatientSerializer(patient, data=request.data)  # FIXED
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Success", "data": serializer.data})
        return Response({"message": "Error", "data": serializer.errors})
    except Patient.DoesNotExist:
        return Response({"message": "Error", "data": "Patient not found"})

@api_view(['DELETE'])
def deletePatient(request, id):
    try:
        patient = Patient.objects.get(id=id)  # FIXED
        patient.delete()  # FIXED
        return Response({"message": "Success", "data": {}})
    except Patient.DoesNotExist:
        return Response({"message": "Error", "data": "Patient not found"})
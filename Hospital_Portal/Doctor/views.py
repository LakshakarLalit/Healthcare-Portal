from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def getAll(request):
    return Response({'message': "Success", })

@api_view(['GET'])
def getById(request, id):
    return

@api_view(['POST'])
def addDoctor(request):
    return Response({"message": "Successfully Added"})

@api_view(['PUT'])
def updateDoctor(request, id):
    return Response({'message': 'updated'})

@api_view(['DELETE'])
def deleteDoctor(request, id):
    return Response({'message': 'Deleted'})
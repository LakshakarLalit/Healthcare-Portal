from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Appointment
from .serializer import AppointmentSerializer

@api_view(['GET'])
def getAll(request):
    appointments = Appointment.objects.all()
    
    # Optional filtering by doctor or patient
    doctor_id = request.query_params.get('doctor')
    patient_id = request.query_params.get('patient')
    
    if doctor_id:
        appointments = appointments.filter(doctor_id=doctor_id)
    if patient_id:
        appointments = appointments.filter(patient_id=patient_id)
        
    data = AppointmentSerializer(appointments, many=True).data
    return Response({"message": "Success", "data": data})

@api_view(['GET'])
def getById(request, id):
    try:
        appointment = Appointment.objects.get(id=id)
        data = AppointmentSerializer(appointment).data
        return Response({"message": "Success", "data": data})
    except Appointment.DoesNotExist:
        return Response({"message": "Not Found", "data": {}})

@api_view(['POST'])
def bookAppointment(request):
    serializer = AppointmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Successfully Booked", "data": serializer.data})
    return Response({"message": "Error", "data": serializer.errors})

@api_view(['PUT'])
def updateAppointment(request, id):
    try:
        appointment = Appointment.objects.get(id=id)
        serializer = AppointmentSerializer(appointment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Success", "data": serializer.data})
        return Response({"message": "Error", "data": serializer.errors})
    except Appointment.DoesNotExist:
        return Response({"message": "Error", "data": "Appointment not found"})

@api_view(['DELETE'])
def deleteAppointment(request, id):
    try:
        appointment = Appointment.objects.get(id=id)
        appointment.delete()
        return Response({"message": "Success", "data": {}})
    except Appointment.DoesNotExist:
        return Response({"message": "Error", "data": "Appointment not found"})

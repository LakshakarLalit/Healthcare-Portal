from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from Doctor.models import Doctor
from Patient.models import Patient
from Appointment.models import Appointment
from datetime import datetime

@api_view(['GET'])
def api_doctors(request):
    doctors = Doctor.objects.all()
    data = []
    for d in doctors:
        data.append({
            "id": d.id,
            "name": d.name,
            "experience": f"{d.experience} Yrs Exp",
            "fee": f"₹{500 + d.experience * 50}",
            "desc": d.about,
            "img": d.avatar or "https://images.unsplash.com/photo-1622253692010-333f2da6031d?auto=format&fit=crop&w=600&q=80",
            "specialty": d.specilization or "General Medicine"
        })
    return Response(data)

@api_view(['GET', 'POST'])
def api_appointments(request):
    if request.method == 'GET':
        appointments = Appointment.objects.all()
        data = []
        for a in appointments:
            patient_name = a.patient.name if a.patient else "Unknown Patient"
            patient_age = a.patient.age if a.patient else 0
            patient_gender = a.patient.gender if a.patient else "Other"
            patient_disease = a.symptoms or (a.patient.disease if a.patient else "General Checkup")
            doc_name = a.doctor.name if a.doctor else "Unassigned"
            if doc_name != "Unassigned" and not doc_name.lower().startswith("dr."):
                doc_name = "Dr. " + doc_name
                
            # Map status
            status_text = a.status
            if a.status == 'Approved':
                status_text = 'Admitted'
            elif a.status == 'Pending':
                status_text = 'Observation'
            elif a.status == 'Completed':
                status_text = 'Discharged'
            elif a.status == 'Cancelled':
                status_text = 'Critical'

            data.append({
                "id": f"PT-{a.patient.id if a.patient else a.id}",
                "name": patient_name,
                "age": patient_age,
                "gender": patient_gender,
                "disease": patient_disease,
                "doctor": doc_name,
                "admissionDate": str(a.date),
                "status": status_text
            })
        return Response(data)
        
    elif request.method == 'POST':
        doctor_id = request.data.get('doctor')
        date_str = request.data.get('date')
        time_slot = request.data.get('time')
        patient_name = request.data.get('patient_name')
        patient_age = request.data.get('patient_age')
        patient_gender = request.data.get('patient_gender')
        
        try:
            doctor = Doctor.objects.get(id=doctor_id)
        except Doctor.DoesNotExist:
            return Response({"error": f"Doctor with id {doctor_id} not found"}, status=status.HTTP_400_BAD_REQUEST)
            
        # Get or create the patient profile
        patient, created = Patient.objects.get_or_create(
            name=patient_name,
            defaults={
                "age": int(patient_age) if patient_age else 30,
                "gender": patient_gender or "Other",
                "disease": "General Consultation",
                "city": "Mumbai",
                "state": "Maharashtra",
                "phone": "9999999999",
                "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?auto=format&fit=crop&w=256&h=256&q=80"
            }
        )
        
        # Parse date
        try:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
        except Exception:
            date_obj = datetime.now().date()
            
        # Create appointment record
        appointment = Appointment.objects.create(
            doctor=doctor,
            patient=patient,
            date=date_obj,
            time_slot=time_slot or "10:00 AM - 10:30 AM",
            status="Pending",
            symptoms="General Checkup"
        )
        
        return Response({
            "message": "Successfully Booked",
            "appointment_id": appointment.id
        }, status=status.HTTP_201_CREATED)

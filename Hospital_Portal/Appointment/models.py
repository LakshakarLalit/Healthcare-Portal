from django.db import models
from Doctor.models import Doctor
from Patient.models import Patient

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    date = models.DateField()
    time_slot = models.CharField(max_length=100)  # e.g., "10:00 AM - 10:30 AM"
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    symptoms = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Appointment: {self.patient.name} with Dr. {self.doctor.name} on {self.date}"

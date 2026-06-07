# import os
# import django

# # Setup Django environment
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Hospital_Portal.settings')
# django.setup()

# from Doctor.models import Doctor
# from Patient.models import Patient
# from Appointment.models import Appointment
# from datetime import date

# def seed():
#     print("Clearing existing database records...")
#     Appointment.objects.all().delete()
#     Doctor.objects.all().delete()
#     Patient.objects.all().delete()

#     print("Adding Indian Doctors...")
#     d1 = Doctor.objects.create(
#         id=1,
#         name="Dr. Firoz Sharma",
#         experience=15,
#         degree="MD, DM",
#         about="Senior Consultant Cardiologist specializing in interventional cardiology, heart failure management, and preventive heart care.",
#         avatar="https://images.unsplash.com/photo-1622253692010-333f2da6031d?auto=format&fit=crop&w=600&q=80",
#         specilization="Cardiology",
#         hospital_name="Metro Hospital"
#     )
#     d2 = Doctor.objects.create(
#         id=2,
#         name="Dr. Ananya Iyer",
#         experience=10,
#         degree="MD, DCH",
#         about="Dedicated Pediatrician expert in infant care, childhood nutrition, vaccination guidelines, and developmental pediatric care.",
#         avatar="https://images.unsplash.com/photo-1594824813573-246434de83fb?auto=format&fit=crop&w=600&q=80",
#         specilization="Pediatrics",
#         hospital_name="Hope Clinic"
#     )
#     d3 = Doctor.objects.create(
#         id=3,
#         name="Dr. Vikram Roy",
#         experience=12,
#         degree="MD, DM",
#         about="Acclaimed Neurologist specializing in neurodegenerative disorders, stroke treatment, chronic migraines, and sleep disorders.",
#         avatar="https://images.unsplash.com/photo-1537368910025-700350fe46c7?auto=format&fit=crop&w=600&q=80",
#         specilization="Neurology",
#         hospital_name="Metro Hospital"
#     )
#     d4 = Doctor.objects.create(
#         id=4,
#         name="Dr. Sneha Kapoor",
#         experience=8,
#         degree="MD, DNB",
#         about="Consultant Dermatologist and Trichologist focused on clinical dermatology, acne treatments, hair restoration, and laser therapies.",
#         avatar="https://images.unsplash.com/photo-1559839734-2b71ea197ec2?auto=format&fit=crop&w=600&q=80",
#         specilization="Dermatology",
#         hospital_name="Skin & Care Clinic"
#     )
#     d5 = Doctor.objects.create(
#         id=5,
#         name="Dr. Rahul Verma",
#         experience=14,
#         degree="MS, MCh",
#         about="Expert Orthopedic Surgeon specializing in joint replacement surgeries, sports injuries, and advanced arthroscopic interventions.",
#         avatar="https://images.unsplash.com/photo-1612349317150-e413f6a5b16d?auto=format&fit=crop&w=600&q=80",
#         specilization="Orthopedics",
#         hospital_name="City Ortho Care"
#     )
#     d6 = Doctor.objects.create(
#         id=6,
#         name="Dr. Priya Patel",
#         experience=9,
#         degree="MBBS, MD",
#         about="Compassionate General Physician addressing chronic illness management, infectious diseases, and general health diagnostics.",
#         avatar="https://images.unsplash.com/photo-1527613426441-4da17471b66d?auto=format&fit=crop&w=600&q=80",
#         specilization="General Medicine",
#         hospital_name="Metro Hospital"
#     )

#     print("Adding Indian Patients...")
#     p1 = Patient.objects.create(
#         id=101,
#         name="Ramesh Sharma",
#         age=45,
#         gender="Male",
#         disease="Coronary Artery Disease",
#         avatar="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=256&h=256&q=80",
#         city="Mumbai",
#         state="Maharashtra",
#         phone="9876543210"
#     )
#     p2 = Patient.objects.create(
#         id=102,
#         name="Aarav Patel",
#         age=6,
#         gender="Male",
#         disease="Acute Bronchitis",
#         avatar="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=256&h=256&q=80",
#         city="Ahmedabad",
#         state="Gujarat",
#         phone="9876543211"
#     )
#     p3 = Patient.objects.create(
#         id=103,
#         name="Meera Nair",
#         age=34,
#         gender="Female",
#         disease="Chronic Migraine",
#         avatar="https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=256&h=256&q=80",
#         city="Kochi",
#         state="Kerala",
#         phone="9876543212"
#     )
#     p4 = Patient.objects.create(
#         id=104,
#         name="Kriti Sen",
#         age=28,
#         gender="Female",
#         disease="Atopic Dermatitis",
#         avatar="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?auto=format&fit=crop&w=256&h=256&q=80",
#         city="Kolkata",
#         state="West Bengal",
#         phone="9876543213"
#     )
#     p5 = Patient.objects.create(
#         id=105,
#         name="Vijay Malhotra",
#         age=58,
#         gender="Male",
#         disease="Osteoarthritis",
#         avatar="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?auto=format&fit=crop&w=256&h=256&q=80",
#         city="Delhi",
#         state="Delhi",
#         phone="9876543214"
#     )
#     p6 = Patient.objects.create(
#         id=106,
#         name="Suman Rao",
#         age=49,
#         gender="Female",
#         disease="Pneumonia",
#         avatar="https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&w=256&h=256&q=80",
#         city="Jaipur",
#         state="Rajasthan",
#         phone="9876543215"
#     )

#     print("Adding Sample Appointments...")
#     Appointment.objects.create(
#         id=1,
#         doctor=d1,
#         patient=p1,
#         date=date(2026, 5, 15),
#         time_slot="10:00 AM - 10:30 AM",
#         status="Approved",
#         symptoms="Coronary Artery Disease"
#     )
#     Appointment.objects.create(
#         id=2,
#         doctor=d2,
#         patient=p2,
#         date=date(2026, 6, 1),
#         time_slot="11:00 AM - 11:30 AM",
#         status="Completed",
#         symptoms="Acute Bronchitis"
#     )
#     Appointment.objects.create(
#         id=3,
#         doctor=d3,
#         patient=p3,
#         date=date(2026, 5, 28),
#         time_slot="02:00 PM - 02:30 PM",
#         status="Pending",
#         symptoms="Chronic Migraine"
#     )
#     Appointment.objects.create(
#         id=4,
#         doctor=d4,
#         patient=p4,
#         date=date(2026, 6, 2),
#         time_slot="03:00 PM - 03:30 PM",
#         status="Pending",
#         symptoms="Atopic Dermatitis"
#     )
#     Appointment.objects.create(
#         id=5,
#         doctor=d5,
#         patient=p5,
#         date=date(2026, 5, 10),
#         time_slot="10:00 AM - 10:30 AM",
#         status="Approved",
#         symptoms="Osteoarthritis"
#     )
#     Appointment.objects.create(
#         id=6,
#         doctor=d6,
#         patient=p6,
#         date=date(2026, 5, 24),
#         time_slot="12:00 PM - 12:30 PM",
#         status="Cancelled",
#         symptoms="Pneumonia"
#     )
#     print("Database seeding completed successfully!")

# if __name__ == "__main__":
#     seed()

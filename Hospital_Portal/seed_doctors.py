import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Hospital_Portal.settings')
django.setup()

from Doctor.models import Doctor

def seed_doctors():
    print("Clearing existing doctor records...")
    Doctor.objects.all().delete()

    print("Adding default Indian Doctors...")
    Doctor.objects.create(
        id=1,
        name="Dr. Firoz Sharma",
        experience=15,
        degree="MD, DM",
        about="Senior Consultant Cardiologist specializing in interventional cardiology, heart failure management, and preventive heart care.",
        avatar="https://images.unsplash.com/photo-1622253692010-333f2da6031d?auto=format&fit=crop&w=600&q=80",
        specilization="Cardiology",
        hospital_name="Metro Hospital"
    )
    Doctor.objects.create(
        id=2,
        name="Dr. Ananya Iyer",
        experience=10,
        degree="MD, DCH",
        about="Dedicated Pediatrician expert in infant care, childhood nutrition, vaccination guidelines, and developmental pediatric care.",
        avatar="https://images.unsplash.com/photo-1594824813573-246434de83fb?auto=format&fit=crop&w=600&q=80",
        specilization="Pediatrics",
        hospital_name="Hope Clinic"
    )
    Doctor.objects.create(
        id=3,
        name="Dr. Vikram Roy",
        experience=12,
        degree="MD, DM",
        about="Acclaimed Neurologist specializing in neurodegenerative disorders, stroke treatment, chronic migraines, and sleep disorders.",
        avatar="https://images.unsplash.com/photo-1537368910025-700350fe46c7?auto=format&fit=crop&w=600&q=80",
        specilization="Neurology",
        hospital_name="Metro Hospital"
    )
    Doctor.objects.create(
        id=4,
        name="Dr. Sneha Kapoor",
        experience=8,
        degree="MD, DNB",
        about="Consultant Dermatologist and Trichologist focused on clinical dermatology, acne treatments, hair restoration, and laser therapies.",
        avatar="https://images.unsplash.com/photo-1559839734-2b71ea197ec2?auto=format&fit=crop&w=600&q=80",
        specilization="Dermatology",
        hospital_name="Skin & Care Clinic"
    )
    Doctor.objects.create(
        id=5,
        name="Dr. Rahul Verma",
        experience=14,
        degree="MS, MCh",
        about="Expert Orthopedic Surgeon specializing in joint replacement surgeries, sports injuries, and advanced arthroscopic interventions.",
        avatar="https://images.unsplash.com/photo-1612349317150-e413f6a5b16d?auto=format&fit=crop&w=600&q=80",
        specilization="Orthopedics",
        hospital_name="City Ortho Care"
    )
    Doctor.objects.create(
        id=6,
        name="Dr. Priya Patel",
        experience=9,
        degree="MBBS, MD",
        about="Compassionate General Physician addressing chronic illness management, infectious diseases, and general health diagnostics.",
        avatar="https://images.unsplash.com/photo-1527613426441-4da17471b66d?auto=format&fit=crop&w=600&q=80",
        specilization="General Medicine",
        hospital_name="Metro Hospital"
    )
    print("Seeding default doctors successfully completed!")

if __name__ == "__main__":
    seed_doctors()

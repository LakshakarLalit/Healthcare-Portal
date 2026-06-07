let container = document.getElementById("doctorContainer")

async function getData() {
    let data;
    try {
        let res = await fetch("http://localhost:8000/api/doctors/");
        if (!res.ok) throw new Error("Network response was not ok");
        data = await res.json();
    }
    catch (e) {
        console.log("Failed to fetch doctors from backend, using dummy data fallback:", e);
        let dummyDoctors = [
            {
                name: "Dr. Firoz Sharma",
                experience: "15 Yrs Exp",
                fee: "₹1,200",
                desc: "Senior Consultant Cardiologist specializing in interventional cardiology, heart failure management, and preventive heart care.",
                img: "https://images.unsplash.com/photo-1622253692010-333f2da6031d?auto=format&fit=crop&w=600&q=80",
                specialty: "Cardiology"
            },
            {
                name: "Dr. Ananya Iyer",
                experience: "10 Yrs Exp",
                fee: "₹800",
                desc: "Dedicated Pediatrician expert in infant care, childhood nutrition, vaccination guidelines, and developmental pediatric care.",
                img: "https://images.unsplash.com/photo-1594824813573-246434de83fb?auto=format&fit=crop&w=600&q=80",
                specialty: "Pediatrics"
            },
            {
                name: "Dr. Vikram Roy",
                experience: "12 Yrs Exp",
                fee: "₹1,500",
                desc: "Acclaimed Neurologist specializing in neurodegenerative disorders, stroke treatment, chronic migraines, and sleep disorders.",
                img: "https://images.unsplash.com/photo-1537368910025-700350fe46c7?auto=format&fit=crop&w=600&q=80",
                specialty: "Neurology"
            },
            {
                name: "Dr. Sneha Kapoor",
                experience: "8 Yrs Exp",
                fee: "₹900",
                desc: "Consultant Dermatologist and Trichologist focused on clinical dermatology, acne treatments, hair restoration, and laser therapies.",
                img: "https://images.unsplash.com/photo-1559839734-2b71ea197ec2?auto=format&fit=crop&w=600&q=80",
                specialty: "Dermatology"
            },
            {
                name: "Dr. Rahul Verma",
                experience: "14 Yrs Exp",
                fee: "₹1,300",
                desc: "Expert Orthopedic Surgeon specializing in joint replacement surgeries, sports injuries, and advanced arthroscopic interventions.",
                img: "https://images.unsplash.com/photo-1612349317150-e413f6a5b16d?auto=format&fit=crop&w=600&q=80",
                specialty: "Orthopedics"
            },
            {
                name: "Dr. Priya Patel",
                experience: "9 Yrs Exp",
                fee: "₹700",
                desc: "Compassionate General Physician addressing chronic illness management, infectious diseases, and general health diagnostics.",
                img: "https://images.unsplash.com/photo-1527613426441-4da17471b66d?auto=format&fit=crop&w=600&q=80",
                specialty: "General Medicine"
            }
        ];
        data = dummyDoctors;
    }

    display(data);
}

function display(allDoctors) {
    container.innerHTML = "";
    for (let i of allDoctors) {
        container.innerHTML += ` 
        <div class="doctorCard">
            <div class="card-img-wrapper">
                <img src="${i.img}" alt="${i.name}">
                <div class="specialty-badge">${i.specialty}</div>
            </div>
            <div class="card-info">
                <h2>${i.name}</h2>
                <div class="doctor-meta">
                    <span>MD, DM</span>
                    <span class="experience">${i.experience || i.exp}</span>
                </div>
                <p class="desc">${i.desc}</p>
                <div class="card-footer">
                    <div class="fee-container">
                        <span class="fee-label">Consultation</span>
                        <span class="fee-amount">${i.fee}</span>
                    </div>
                    <button><a href="../Appointment/Appointment.html">Book Appointment</a></button>
                </div>
            </div>
        </div>
`;
    }
}

getData();